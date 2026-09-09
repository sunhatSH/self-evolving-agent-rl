"""E13 端到端离线验证：含图轨迹被过滤（不进 PPO）。

不依赖 verl/GPU/沙箱,纯验证 image_trajectory_drop_patch 的 _is_image_trajectory
把「含图轨迹」判为丢弃、纯文本保留。

注:原配套的截图 prompt 注入(CLAgentDataset._inject_screenshot_request)随 CL
数据集模块一并移除,该半边已删,此处仅覆盖存活的含图过滤逻辑。
"""

from __future__ import annotations

from trainer.image_trajectory_drop_patch import _is_image_trajectory


class _Traj:
    def __init__(self, mmd=None, rid=None, rmask=None):
        self.multi_modal_data = mmd
        self.response_ids = rid
        self.response_mask = rmask


def test_screenshot_trajectory_gets_dropped():
    # 模拟：截图 prompt → agent 产图 → 轨迹带 multi_modal_data.images → 判丢弃。
    img_traj = _Traj(mmd={"images": ["<png bytes>"]}, rid=[1, 2, 3], rmask=[1, 1, 1])
    assert _is_image_trajectory(img_traj) is True
    # 对照：同任务纯文本完成(无图) → 保留。
    txt_traj = _Traj(mmd={}, rid=[1, 2, 3], rmask=[1, 1, 1])
    assert _is_image_trajectory(txt_traj) is False


def test_length_mismatch_signals_image():
    # 信号 2：response_ids 与 response_mask 长度不等(视觉 token 展开的直接症状)。
    bad = _Traj(mmd=None, rid=[1, 2, 3, 4], rmask=[1, 1, 1])
    assert _is_image_trajectory(bad) is True
    good = _Traj(mmd=None, rid=[1, 2, 3], rmask=[1, 1, 1])
    assert _is_image_trajectory(good) is False
