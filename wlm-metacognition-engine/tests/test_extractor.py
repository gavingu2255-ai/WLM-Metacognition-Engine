import pytest
from wlm_metacognition_engine.reasoning_extractor import extract_reasoning_steps


def test_extract_reasoning_steps_basic():
    text = "A implies B. B implies C."
    steps = extract_reasoning_steps(text)

    assert steps == ["A implies B", "B implies C"]


def test_extract_reasoning_steps_empty_segments():
    text = "A implies B..  . C follows."
    steps = extract_reasoning_steps(text)

    assert steps == ["A implies B", "C follows"]
