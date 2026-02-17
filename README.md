# WLM‑Metacognition‑Engine  
**Structured metacognition for AI reasoning: paths, consistency, dimension switching**

The **WLM‑Metacognition‑Engine** is the **self‑monitoring and self‑regulation layer** of the WLM ecosystem.  
It structures an AI’s reasoning process into explicit, inspectable, and controllable components.

This is the **sixth major layer** of WLM:

1. SLP‑World‑Interpreter — Language → Structure  
2. WLM‑World‑Model‑Interpreter — World Model → Structure  
3. WLM‑Agent‑Behavior — Structure → Behavior  
4. WLM‑Persona‑Engine — Structure → Identity  
5. WLM‑Knowledge‑Engine — Structure → Knowledge  
6. **WLM‑Metacognition‑Engine — Structure → Self‑Monitoring** ← *this repo*

It provides the missing link between **reasoning** and **reasoning about reasoning**:

> **Structure → Reasoning → Self‑Monitoring → Stability**

---

## ✨ Why this exists

LLMs generate answers, but they do not:

- track their reasoning path  
- detect contradictions  
- maintain dimensional consistency  
- monitor shifts in context  
- regulate their own behavior  
- detect when they are hallucinating  

The WLM‑Metacognition‑Engine fixes this by introducing:

- **structured reasoning paths**  
- **consistency checks**  
- **dimension‑aware reasoning**  
- **self‑evaluation hooks**  
- **metacognitive signals**  
- **reasoning‑state transitions**  

This is the layer that makes AI **transparent, controllable, and stable**.

---

## ✨ Features

### **1. Reasoning Path Extraction**
Every reasoning step is structured into:

- premises  
- transformations  
- inferences  
- conclusions  

### **2. Consistency Checking**
Detects:

- logical contradictions  
- dimensional mismatches  
- invalid inference steps  
- unstable reasoning loops  

### **3. Dimension Switching**
Tracks and regulates transitions between:

- spatial reasoning  
- temporal reasoning  
- causal reasoning  
- physical reasoning  
- identity reasoning  
- knowledge reasoning  

### **4. Metacognitive Signals**
Produces signals such as:

- confidence  
- uncertainty  
- contradiction alerts  
- missing‑information flags  
- reasoning‑depth indicators  

### **5. Deterministic Metacognitive Graph**
Outputs a structured graph representing the AI’s reasoning process.

---

## 🚀 Quickstart

### **Install**

```bash
pip install wlm-metacognition-engine
```

### **Use**

```python
from wlm_metacognition_engine import analyze_reasoning

result = analyze_reasoning("If Earth orbits the Sun, then seasons occur.")
print(result)
```

### **Output (MVP)**

```
{
  "steps": [],
  "consistency": [],
  "dimensions": {},
  "signals": [],
  "metacognitive_graph": {}
}
```

---

## 🧠 How it works

The engine performs five steps:

### **1. Input → Reasoning Trace**
Extracts the implicit reasoning path.

### **2. Trace → Structured Steps**
Normalizes each step into a structural representation.

### **3. Steps → Consistency Analysis**
Checks for contradictions or invalid transitions.

### **4. Steps → Dimensional Analysis**
Identifies which reasoning dimensions are active.

### **5. Steps → Metacognitive Graph**
Builds a graph representing the reasoning process.

---

## 📦 API

### `analyze_reasoning(text: str) → dict`

```python
def analyze_reasoning(text: str) -> dict:
    """
    Analyze reasoning structure and produce metacognitive signals.
    """
```

### MetacognitionGraph structure (MVP)

```json
{
  "steps": [],
  "consistency": [],
  "dimensions": {},
  "signals": [],
  "metacognitive_graph": {}
}
```

---

## 🏗 Repository Structure

```
wlm-metacognition-engine/
│
├── LICENSE
├── README.md
├── pyproject.toml
├── setup.cfg
│
├── src/
│   └── wlm_metacognition_engine/
│       ├── __init__.py
│       ├── api.py
│       ├── reasoning_extractor.py
│       ├── consistency_engine.py
│       ├── dimension_tracker.py
│       ├── signal_engine.py
│       ├── graph_builder.py
│       └── cli.py
│
├── examples/
│   ├── simple_reasoning.md
│   ├── contradiction.md
│   └── dimension_switch.md
│
├── tests/
│   ├── test_extractor.py
│   ├── test_consistency.py
│   ├── test_dimensions.py
│   ├── test_signals.py
│   └── test_end_to_end.py
│
└── docs/
    ├── overview.md
    ├── metacognition-rules.md
    ├── api.md
    └── roadmap.md
```

---

## 📄 License

MIT License  
Copyright (c) 2026  
**Wujie Gu**

---

## 🧩 Summary

The **WLM‑Metacognition‑Engine** is the structural metacognition layer of the WLM ecosystem.  
It turns reasoning into **structured, inspectable, self‑regulated processes**.

It enables:

- transparent reasoning  
- consistent inference  
- dimension‑aware thinking  
- self‑monitoring  
- stable agent behavior  

A foundational component of the **WLM reasoning stack**.
