"""
graph_builder.py — Build a structured metacognition graph.

MVP behavior:
    - Wraps steps, consistency, dimensions, and signals into a graph dict.
"""

def build_metacognition_graph(steps, consistency, dimensions, signals):
    """
    Build a metacognition graph structure.

    Returns
    -------
    dict
        Graph structure.
    """
    return {
        "nodes": steps,
        "edges": [],
        "consistency": consistency,
        "dimensions": dimensions,
        "signals": signals,
    }
