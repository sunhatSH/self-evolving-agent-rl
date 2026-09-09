"""policy_loss_padding_patch 回归测试（需 torch；verl 用 sys.modules 桩注入）。

验证：
  1. ``_reliable_response_lens`` 优先用 old_log_probs（responses 会被 tq 截短）。
  2. ``_patched_no_padding_2_padding`` 按 old_log_probs 长度切 response，不受 responses 截短影响。
  3. ``_pad_to_common`` 把 response_mask/advantages 补到 log_prob 宽。

本测试不 import 真 verl（本机无），用 sys.modules 注入桩模块后再 import patch。
"""
from __future__ import annotations

import importlib.machinery
import sys
import types

import pytest

torch = pytest.importorskip("torch")


def _module(name: str) -> types.ModuleType:
    mod = types.ModuleType(name)
    mod.__spec__ = importlib.machinery.ModuleSpec(name, loader=None)
    mod.__path__ = []  # type: ignore[attr-defined]
    return mod


def _install_verl_stub():
    """注入 patch import 所需的 verl 模块树桩。"""
    if "verl.workers.utils.padding" in sys.modules:
        return

    def _orig(tensor, data):
        raise AssertionError("original no_padding_2_padding should not be called")

    padding = _module("verl.workers.utils.padding")
    padding.no_padding_2_padding = _orig
    losses = _module("verl.workers.utils.losses")
    losses.no_padding_2_padding = _orig

    core_algos = _module("verl.trainer.ppo.core_algos")
    core_algos.agg_loss = lambda **kw: torch.tensor(0.0)
    core_algos.get_policy_loss_fn = lambda mode: (lambda **kw: (torch.tensor(1.0), {"pg_clipfrac": 0.1}))
    core_algos.kl_penalty = lambda **kw: torch.zeros(1)

    metric = _module("verl.utils.metric")
    metric.AggregationType = types.SimpleNamespace(SUM="sum", MEAN="mean")
    metric.Metric = types.SimpleNamespace(from_dict=lambda d, aggregation=None: None)

    ppo = _module("verl.trainer.ppo")
    ppo.core_algos = core_algos
    trainer = _module("verl.trainer")
    trainer.ppo = ppo
    utils = _module("verl.workers.utils")
    utils.padding = padding
    utils.losses = losses
    workers = _module("verl.workers")
    workers.utils = utils
    vutils = _module("verl.utils")
    vutils.metric = metric
    verl = _module("verl")
    verl.workers = workers
    verl.trainer = trainer
    verl.utils = vutils

    for name, mod in [
        ("verl", verl),
        ("verl.workers", workers),
        ("verl.workers.utils", utils),
        ("verl.workers.utils.padding", padding),
        ("verl.workers.utils.losses", losses),
        ("verl.trainer", trainer),
        ("verl.trainer.ppo", ppo),
        ("verl.trainer.ppo.core_algos", core_algos),
        ("verl.utils", vutils),
        ("verl.utils.metric", metric),
    ]:
        sys.modules[name] = mod


def _nested(lens: list[int]) -> torch.Tensor:
    return torch.nested.as_nested_tensor([torch.arange(n, dtype=torch.float) for n in lens], layout=torch.jagged)


def test_reliable_response_lens_uses_old_log_probs():
    _install_verl_stub()
    from trainer import policy_loss_padding_patch as patch

    data = {
        "old_log_probs": _nested([3757, 1562]),
        "response_mask": _nested([3757, 1562]),
        "responses": _nested([1, 1]),  # 模拟 tq 截短
    }
    lens = patch._reliable_response_lens(data)
    assert lens.tolist() == [3757, 1562]


def test_no_padding_2_padding_uses_old_log_probs_not_responses():
    _install_verl_stub()
    from trainer import policy_loss_padding_patch as patch

    prompts = _nested([10, 10])
    old_log_probs = _nested([3757, 1562])
    log_probs = _nested([10 + 3757, 10 + 1562])  # prompt+response 全长
    data = {
        "prompts": prompts,
        "old_log_probs": old_log_probs,
        "response_mask": _nested([3757, 1562]),
        "advantages": _nested([3757, 1562]),
        "responses": _nested([1, 1]),  # 截短：若误用 responses 会切出长度 1
    }
    out = patch._patched_no_padding_2_padding(log_probs, data)
    assert out.shape == (2, 3757)
    # row0 应有 3757 个真实 log_prob（非退化成 1）
    assert (out[0] != 0).sum().item() == 3757


def test_pad_to_common_aligns_fields():
    _install_verl_stub()
    from trainer import policy_loss_padding_patch as patch

    class _D(dict):
        pass

    data = _D(
        response_mask=torch.ones(8, 13571, dtype=torch.long),
        old_log_probs=torch.zeros(8, 15769),
        advantages=torch.zeros(8, 13571),
    )
    log_prob = torch.zeros(8, 15769)
    patch._pad_to_common(data, log_prob)
    assert data["response_mask"].shape == (8, 15769)
    assert data["old_log_probs"].shape == (8, 15769)
    assert data["advantages"].shape == (8, 15769)
    assert data["response_mask"][:, 13571:].sum() == 0
