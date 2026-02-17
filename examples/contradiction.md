# Example: Contradiction  
**Reasoning → Steps → (Future) Consistency Detection**

This example shows how the engine handles contradictory statements.

---

## Input

```
A is true. A is false.
```

---

## Code

```python
from wlm_metacognition_engine import analyze_reasoning

result = analyze_reasoning("A is true. A is false.")
print(result)
```

---

## Output (MVP)

```
{
  "steps": ["A is true", "A is false"],
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
  "metacognitive_graph": {
    "nodes": ["A is true", "A is false"],
    "edges": [],
    "consistency": [],
    "dimensions": {
      "spatial": [],
      "temporal": [],
      "causal": [],
      "physical": [],
      "identity": [],
      "knowledge": []
    },
    "signals": []
  }
}
```

---

## Explanation

In the MVP:

- **Steps** are extracted  
- **Consistency** remains empty (no contradiction detection yet)  

Future versions will detect:

- direct contradictions  
- logical impossibilities  
- reasoning‑loop conflicts  
