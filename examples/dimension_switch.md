# Example: Dimension Switching  
**Reasoning → Steps → (Future) Dimension Tracking**

This example shows how the engine handles reasoning that spans multiple dimensions.

---

## Input

```
The ball rolls downhill because of gravity. After 5 seconds it reaches the bottom.
```

---

## Code

```python
from wlm_metacognition_engine import analyze_reasoning

result = analyze_reasoning(
    "The ball rolls downhill because of gravity. After 5 seconds it reaches the bottom."
)
print(result)
```

---

## Output (MVP)

```
{
  "steps": [
    "The ball rolls downhill because of gravity",
    "After 5 seconds it reaches the bottom"
  ],
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
    "nodes": [
      "The ball rolls downhill because of gravity",
      "After 5 seconds it reaches the bottom"
    ],
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

- **Steps** extracted  
- **Dimensions** empty  

Future versions will detect:

- **causal** reasoning (gravity → motion)  
- **physical** reasoning (downhill motion)  
- **temporal** reasoning (5‑second interval)  
- **spatial** reasoning (downhill → bottom)  

This is where the metacognition layer becomes powerful.
