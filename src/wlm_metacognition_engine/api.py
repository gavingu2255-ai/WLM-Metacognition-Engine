"""
High‑level API for WLM‑Metacognition‑Engine.

This module exposes a single entry point:

    analyze_reasoning(text) -> MetacognitionGraph

MVP behavior:
    - Returns a deterministic metacognition structure.
"""

from .reasoning_extractor import extract_reasoning_steps
from .consistency_engine import check_consistency
from .dimension_tracker import track_dimensions
from .signal_engine import generate_signals
from .graph_builder import build_metacognition_graph


def analyze_reasoning(text: str) -> dict:
    """
    Analyze reasoning structure and produce metacognitive signals.

    Parameters
    ----------
    text : str
        Input text representing reasoning or explanation.

    Returns
    -------
    dict
        MetacognitionGraph structure.
    """
    steps = extract_reasoning_steps(text)
    consistency = check_consistency(steps)
    dimensions = track_dimensions(steps)
    signals = generate_signals(steps, consistency, dimensions)
    graph = build_metacognition_graph(steps, consistency, dimensions, signals)

    return {
        "steps": steps,
        "consistency": consistency,
        "dimensions": dimensions,
        "signals": signals,
        "metacognitive_graph": graph,
    }
