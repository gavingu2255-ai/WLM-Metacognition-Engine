import pytest
from wlm_metacognition_engine.dimension_tracker import track_dimensions


def test_dimension_tracker_mvp():
    dims = track_dimensions(["A implies B"])

    assert isinstance(dims, dict)
    assert "spatial" in dims
    assert "temporal" in dims
    assert "causal" in dims
    assert "physical" in dims
    assert "identity" in dims
    assert "knowledge" in dims

    # MVP: all empty lists
    assert dims["spatial"] == []
    assert dims["temporal"] == []
    assert dims["causal"] == []
    assert dims["physical"] == []
    assert dims["identity"] == []
    assert dims["knowledge"] == []
