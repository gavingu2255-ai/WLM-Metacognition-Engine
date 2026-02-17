import pytest
from wlm_metacognition_engine.consistency_engine import check_consistency


def test_consistency_mvp():
    steps = ["A implies B", "B implies C"]
    issues = check_consistency(steps)

    assert issues == []  # MVP: no consistency checks yet
