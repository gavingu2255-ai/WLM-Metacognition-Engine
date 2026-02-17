# API Specification — WLM‑Metacognition‑Engine  
**Public API for analyzing reasoning and generating metacognitive structure**

This document defines the official API surface for WLM‑Metacognition‑Engine.

The API is intentionally minimal, deterministic, and stable.

---

# 1. High‑Level API

The primary entry point is:

```python
analyze_reasoning(text) -> dict
```

### Description
Analyze reasoning structure and produce metacognitive signals.

### Signature

```python
def analyze_reasoning(text: str) -> dict:
    """
    Analyze reasoning structure and produce metacognitive signals.
    """
```

### Parameters

| Name | Type | Description |
|------|------|-------------|
| `text` | `str` | Input reasoning text |

### Returns

| Type | Description |
|------|-------------|
| `dict` | MetacognitionGraph structure |

---

# 2. MetacognitionGraph Structure

```json
{
  "steps": [],
  "consistency": [],
  "dimensions": {
    "spatial": [],
    "temporal": [],
    "causal": [],
    "physical": [],
    "identity": [],
    "knowledge": []
  },
  "signals": [],
  "metacognitive_graph": {}
}
```

---

# 3. CLI API

The library provides a command‑line interface:

```
wlm-metacognition analyze <input>
```

### Usage

```
wlm-metacognition analyze "A implies B. B implies C."
wlm-metacognition analyze input.txt
wlm-metacognition analyze input.txt --out output.json
```

---

# 4. Error Handling

- deterministic behavior  
- no silent failures  
- clear error messages  
- no partial graphs  

---

# 5. Versioning

Semantic versioning:

- `0.x` — experimental  
- `1.x` — reasoning‑path extraction  
- `2.x` — contradiction detection + dimension inference  

---

# 6. Summary

The WLM‑Metacognition‑Engine exposes a single stable entry point:

```
analyze_reasoning(text) → MetacognitionGraph
```

This enables structured, deterministic, self‑regulated reasoning.
