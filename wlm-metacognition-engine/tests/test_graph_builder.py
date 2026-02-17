import pytest
from wlm_metacognition_engine.graph_builder import build_metacognition_graph


def test_graph_builder_basic():
    steps = ["A implies B"]
    consistency = []
    dimensions = {"spatial": [], "temporal": [], "causal": [], "physical": [], "identity": [], "knowledge": []}
    signals = []

    graph = build_metacognition_graph(steps, consistency, dimensions, signals)

    assert graph["nodes"] == steps
    assert graph["edges"] == []
    assert graph["consistency"] == consistency
    assert graph["dimensions"] == dimensions
    assert graph["signals"] == signals
