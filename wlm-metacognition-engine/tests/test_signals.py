import pytest
from wlm_metacognition_engine.signal_engine import generate_signals


def test_signal_engine_mvp():
    steps = ["A implies B"]
    signals = generate_signals(steps, [], {})

    assert signals == []  # MVP: no signals generated
