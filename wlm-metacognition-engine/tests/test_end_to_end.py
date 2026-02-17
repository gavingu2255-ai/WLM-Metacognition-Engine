import pytest
from wlm_metacognition_engine.api import analyze_reasoning


def test_end_to_end_analysis():
    text = "A implies B. B implies C."

    result = analyze_reasoning(text)

    assert result["steps"] == ["A implies B", "B implies C"]
    assert result["consistency"] == []
    assert "spatial" in result["dimensions"]
    assert result["signals"] == []
    assert isinstance(result["metacognitive_graph"], dict)
