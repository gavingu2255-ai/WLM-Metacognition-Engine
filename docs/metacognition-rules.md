# Metacognition Rules — WLM‑Metacognition‑Engine  
**How reasoning becomes structured, inspectable, and self‑regulated**

This document defines the rules that convert raw reasoning text into  
steps, consistency checks, dimensions, signals, and a metacognitive graph.

The rules are deterministic, structural, and model‑agnostic.

---

# 1. Reasoning Step Rules

Reasoning steps are the **atomic units** of thought.

Examples:

- “A implies B”  
- “Therefore B implies C”  
- “Thus C must be true”  

### MVP extraction

- split on periods  
- trim whitespace  
- ignore empty segments  

Future versions will include:

- logical operator detection  
- premise/conclusion tagging  
- inference type classification  

---

# 2. Consistency Rules

Consistency checks detect:

- contradictions  
- invalid inference transitions  
- circular reasoning  
- unsupported conclusions  

### MVP behavior

- no consistency checks yet  

Future versions will include:

- contradiction detection  
- inference validation  
- reasoning‑loop detection  

---

# 3. Dimension Rules

Dimensions represent **types of reasoning**:

- **Spatial** — topology, location, geometry  
- **Temporal** — sequence, duration, simultaneity  
- **Causal** — cause/effect, mechanisms  
- **Physical** — forces, constraints, affordances  
- **Identity** — self, roles, agents  
- **Knowledge** — facts, uncertainty, epistemic state  

### MVP behavior

- all dimensions returned as empty lists  

Future versions will infer dimensions from reasoning content.

---

# 4. Signal Rules

Signals represent **metacognitive indicators**:

- confidence  
- uncertainty  
- contradiction alerts  
- missing‑information flags  
- reasoning‑depth indicators  

### MVP behavior

- no signals generated yet  

---

# 5. Metacognition Graph Rules

The metacognition graph represents:

- nodes = reasoning steps  
- edges = inferred transitions  
- consistency = issues  
- dimensions = active reasoning types  
- signals = metacognitive indicators  

### MVP behavior

- nodes only  
- no edges  

---

# 6. Determinism

Metacognition must be:

- deterministic  
- reproducible  
- structurally grounded  
- consistent across runs  

Same input → same metacognition graph.

---

# 7. Future Extensions

- reasoning‑path extraction  
- contradiction detection  
- dimension inference  
- metacognitive signal generation  
- multi‑step reasoning graph construction  
