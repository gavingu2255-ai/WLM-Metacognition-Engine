"""
dimension_tracker.py — Track reasoning dimensions.

MVP behavior:
    - No real dimension detection.
    - Returns empty dimension maps.
"""

def track_dimensions(steps):
    """
    Track which reasoning dimensions are active.

    Returns
    -------
    dict
        Dimension annotations (MVP: empty).
    """
    return {
        "spatial": [],
        "temporal": [],
        "causal": [],
        "physical": [],
        "identity": [],
        "knowledge": [],
    }
