# Example: Simple Reasoning  
**Reasoning → Steps → Metacognition Graph**

This example shows how the engine extracts reasoning steps from a simple chain.

---

## Input

```
A implies B. B implies C.
```

---

## Code

```python
from wlm_metacognition_engine import analyze_reasoning

result = analyze_reasoning("A implies B. B implies C.")
print(result)
```

---

## Output (MVP)

```
{
  "steps": ["A implies B", "B implies C"],
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
    "nodes": ["A implies B", "B implies C"],
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

- **Steps** = each sentence becomes a reasoning unit  
- **Consistency** = no checks yet  
- **Dimensions** = empty  
- **Signals** = empty  
- **Graph** = nodes only  

Future versions will infer:

- causal transitions  
- inference types  
- reasoning edges  
