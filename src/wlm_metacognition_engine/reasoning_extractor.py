"""
reasoning_extractor.py — Extract reasoning steps from text.

MVP behavior:
    - Split text into sentences.
    - Treat each sentence as a "step".
    - No semantic parsing yet.
"""

def extract_reasoning_steps(text: str):
    """
    Extract reasoning steps from text.

    MVP:
        - Split on periods.
        - Strip whitespace.
        - Ignore empty segments.

    Returns
    -------
    list
        List of reasoning steps.
    """
    raw_steps = [s.strip() for s in text.split(".")]
    steps = [s for s in raw_steps if s]
    return steps
