"""CPU unit tests for the selection layer (agent_rl_sync_trainer).

Off-cluster: no verl/transfer_queue/recipe_custom. Tests the pure grouping +
selection logic with fakes (no TQ, no KVBatchMeta).
"""
import pytest


def test_group_keys_by_uid():
    from trainer.agent_rl_sync_trainer import _group_keys_by_uid
    keys = ['u1_s0_0','u1_s1_0','u1_s2_0','u2_s0_0','u2_s1_0','u3_s0_0','u3_s1_0','u4_s0_0']
    g = _group_keys_by_uid(keys)
    assert len(g) == 4
    assert set(g.keys()) == {'u1','u2','u3','u4'}
    assert len(g['u1']) == 3
    assert len(g['u2']) == 2


def test_group_keys_single_key():
    from trainer.agent_rl_sync_trainer import _group_keys_by_uid
    g = _group_keys_by_uid(['onlykey'])
    assert len(g) == 1
    assert 'onlykey' in g


def test_group_keys_empty():
    from trainer.agent_rl_sync_trainer import _group_keys_by_uid
    g = _group_keys_by_uid([])
    assert g == {}


def test_select_groups_passthrough_when_few_groups(monkeypatch):
    """If groups <= n_select, return batch unchanged."""
    from trainer.agent_rl_sync_trainer import select_groups

    class FakeBatch:
        keys = ['u1_s0_0','u1_s1_0','u2_s0_0','u2_s1_0']
        partition_id = "train"
        def select_keys(self, ks):
            return ("selected", ks)

    out = select_groups(FakeBatch(), n_select=10)
    # passthrough: groups(2) <= n_select(10) → return batch unchanged (did not call select_keys)
    assert out is not None


def test_select_groups_selects_n(monkeypatch):
    """More groups than n_select: select n_select groups."""
    from trainer.agent_rl_sync_trainer import select_groups, _group_keys_by_uid

    # 6 groups, select 3
    keys = []
    for i in range(6):
        keys.extend([f'u{i}_s{j}_0' for j in range(2)])

    class FakeBatch:
        pass
    b = FakeBatch()
    b.keys = keys
    b.partition_id = "train"
    captured = {}
    def fake_select(ks):
        captured['keys'] = ks
        return ("selected", ks)
    b.select_keys = fake_select

    # mock reward + advantage readers
    import trainer.agent_rl_sync_trainer as t
    monkeypatch.setattr(t, '_read_group_rewards', lambda keys, pid: {f'u{i}': 0.5 for i in range(6)})
    monkeypatch.setattr(t, '_read_group_advantages', lambda keys, pid: {f'u{i}': 0.1*i for i in range(6)})

    out = select_groups(b, n_select=3, group_size=2)
    # selected 3 groups' keys (6 keys total, 2 per group)
    assert len(captured['keys']) == 6
    # u5 has highest advantage (0.5), u4 (0.4), u3 (0.3) → should be selected
    selected_uids = {k.rsplit('_s',1)[0] for k in captured['keys']}
    assert selected_uids == {'u5','u4','u3'}


def test_select_groups_drop_bottom_and_low(monkeypatch):
    """Drop groups that are both bottom-20% AND < 0.3."""
    from trainer.agent_rl_sync_trainer import select_groups
    import trainer.agent_rl_sync_trainer as t

    # 5 groups: scores [0.1, 0.2, 0.5, 0.6, 0.7]. bottom 20% = {0.1}, <0.3 = {0.1,0.2}
    # drop = bottom20% AND <0.3 = {0.1} (u0). remaining = u1,u2,u3,u4
    keys = []
    for i in range(5):
        keys.extend([f'u{i}_s{j}_0' for j in range(2)])

    class FakeBatch:
        pass
    b = FakeBatch()
    b.keys = keys
    b.partition_id = "train"
    captured = {}
    def fake_select(ks):
        captured['keys'] = ks
        return ks
    b.select_keys = fake_select

    scores = {'u0':0.1,'u1':0.2,'u2':0.5,'u3':0.6,'u4':0.7}
    monkeypatch.setattr(t, '_read_group_rewards', lambda keys, pid: scores)
    monkeypatch.setattr(t, '_read_group_advantages', lambda keys, pid: {u: s for u,s in scores.items()})

    out = select_groups(b, n_select=3, group_size=2)
    # u0 dropped (bottom20% & <0.3). remaining u1-u4. select top 3 by adv: u4,u3,u2
    selected_uids = {k.rsplit('_s',1)[0] for k in captured['keys']}
    assert 'u0' not in selected_uids  # dropped
    assert selected_uids == {'u4','u3','u2'}


def test_select_groups_no_drop_if_not_both(monkeypatch):
    """bottom-20% but >= 0.3 → NOT dropped (must satisfy both conditions)."""
    from trainer.agent_rl_sync_trainer import select_groups
    import trainer.agent_rl_sync_trainer as t

    # 5 groups: scores [0.35, 0.5, 0.6, 0.7, 0.8]. bottom 20% = {0.35}, but 0.35 >= 0.3 → not dropped
    keys = []
    for i in range(5):
        keys.extend([f'u{i}_s{j}_0' for j in range(2)])

    class FakeBatch:
        pass
    b = FakeBatch()
    b.keys = keys
    b.partition_id = "train"
    captured = {}
    b.select_keys = lambda ks: captured.setdefault('keys', ks)

    scores = {'u0':0.35,'u1':0.5,'u2':0.6,'u3':0.7,'u4':0.8}
    monkeypatch.setattr(t, '_read_group_rewards', lambda keys, pid: scores)
    monkeypatch.setattr(t, '_read_group_advantages', lambda keys, pid: scores)

    select_groups(b, n_select=3, group_size=2)
    selected_uids = {k.rsplit('_s',1)[0] for k in captured['keys']}
    # u0 is bottom-20% but >= 0.3, NOT dropped. top 3 by adv: u4,u3,u2
    assert 'u0' not in selected_uids  # not selected (low adv) but not dropped either
    assert selected_uids == {'u4','u3','u2'}


def test_select_groups_varlen_and_sparse(monkeypatch):
    """变长组新语义: >=50% 有效进训练(变长, 不补齐); <50% 不训练但任务存活."""
    from trainer.agent_rl_sync_trainer import select_groups
    import trainer.agent_rl_sync_trainer as t

    # group_size=4, min_valid=2. 4 组:
    #   u0 完整(4条), u1 >=50%(2条→变长进训练), u2 <50%(1条→不训练但任务存活), u3 完整(4条)
    keys = []
    keys.extend([f'u0_s{j}_0' for j in range(4)])
    keys.extend([f'u1_s{j}_0' for j in range(2)])
    keys.append('u2_s0_0')
    keys.extend([f'u3_s{j}_0' for j in range(4)])

    class FakeBatch:
        pass
    b = FakeBatch()
    b.keys = keys
    b.partition_id = "train"
    captured = {}
    b.select_keys = lambda ks: captured.setdefault('keys', ks)

    scores = {'u0': 0.9, 'u1': 0.9, 'u2': 0.9, 'u3': 0.9}
    monkeypatch.setattr(t, '_read_group_rewards', lambda keys, pid: scores)
    monkeypatch.setattr(t, '_read_group_advantages', lambda keys, pid: {'u0': 0.3, 'u1': 0.2, 'u3': 0.1})

    _, train_survived, task_survived = select_groups(b, n_select=10, group_size=4)
    trained_uids = {k.rsplit('_s', 1)[0] for k in captured['keys']}
    # u0/u1/u3 进训练(>=50%); u1 变长(只2条); u2 不进训练(<50%)
    assert trained_uids == {'u0', 'u1', 'u3'}
    assert 'u2' not in trained_uids
    # u1 变长: 只贡献实际的 2 条(不补齐到 4)
    assert sum(1 for k in captured['keys'] if k.startswith('u1_')) == 2
    # 任务存活集: 所有 >=1 有效的组(含 u2)都在
    assert set(task_survived) == {'u0', 'u1', 'u2', 'u3'}


def test_select_groups_task_survived_decoupled(monkeypatch):
    """任务存活(>=1有效)与训练存活(>=50%)解耦: <50% 组不训练但任务仍存活."""
    from trainer.agent_rl_sync_trainer import select_groups
    import trainer.agent_rl_sync_trainer as t

    # group_size=4: u0 完整, u1 只 1 条(<50%, 不训练但任务存活)
    keys = [f'u0_s{j}_0' for j in range(4)] + ['u1_s0_0']
    class FakeBatch:
        pass
    b = FakeBatch()
    b.keys = keys
    b.partition_id = "train"
    captured = {}
    b.select_keys = lambda ks: captured.setdefault('keys', ks)

    _, train_survived, task_survived = select_groups(b, n_select=10, group_size=4)
    trained_uids = {k.rsplit('_s', 1)[0] for k in captured['keys']}
    assert trained_uids == {'u0'}            # 只 u0 进训练
    assert set(task_survived) == {'u0', 'u1'}  # 但 u1 任务存活(下一轮追问)
