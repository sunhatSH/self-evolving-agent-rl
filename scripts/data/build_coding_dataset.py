"""从 CL 数据集抽取 coding 子集，重构为本项目的 50 步训练数据集。

目的: 验证系统端到端可用(非能力提升)。只用 coding, 训 50 步。
  50 步 × 每步 64 组 = 3200 条 → 正好 CL 数据集里 coding 的全部。

来源: agentic_cl_research/datasets/train_cl.parquet (6400 = coding 3200 + office 3200)
输出: datasets/train_coding_3200.parquet (coding 全 3200 条)

schema 两边完全一致(prompt/data_source/reward_model/bucket/extra_info),
reward_fn 同指向 trainer.model_reward_omni.compute_score, 无需改字段, 只筛 bucket==coding。
"""
from __future__ import annotations

import argparse
import os

import pandas as pd

_SRC = "/mnt/afs_toolcall/sunhao4/workspace/agentic_cl_research/datasets/train_cl.parquet"
_OUT = os.path.join(os.path.dirname(__file__), "..", "..", "datasets", "train_coding_3200.parquet")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=_SRC, help="CL 源数据集 parquet")
    ap.add_argument("--out", default=_OUT, help="输出 parquet")
    ap.add_argument("--n", type=int, default=3200, help="取多少条 coding(默认全 3200=50步×64)")
    ap.add_argument("--shuffle", action="store_true", help="打乱(默认不乱, 保持难度混杂的原序)")
    args = ap.parse_args()

    df = pd.read_parquet(args.src)
    cod = df[df["bucket"] == "coding"].reset_index(drop=True)
    print(f"源 coding 总数: {len(cod)}")

    if args.shuffle:
        cod = cod.sample(frac=1.0, random_state=42).reset_index(drop=True)
    out = cod.iloc[: args.n].reset_index(drop=True)

    # 难度分布报告(确认混杂性)
    import collections
    diffs = collections.Counter(e.get("difficulty") for e in out["extra_info"])
    print(f"取出 {len(out)} 条; difficulty 分布: {dict(sorted(diffs.items()))}")

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    out.to_parquet(args.out, index=False)
    print(f"saved {os.path.abspath(args.out)}")


if __name__ == "__main__":
    main()
