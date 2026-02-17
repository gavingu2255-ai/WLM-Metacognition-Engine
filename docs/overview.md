# WLM‑Metacognition‑Engine — Overview  
**Reasoning → Structure → Self‑Monitoring → Stability**

The **WLM‑Metacognition‑Engine** is the self‑monitoring and self‑regulation layer of the WLM ecosystem.  
It structures an AI’s reasoning process into explicit, inspectable, and controllable components.

This is the **sixth major layer** of WLM:

1. SLP‑World‑Interpreter — Language → Structure  
2. WLM‑World‑Model‑Interpreter — World Model → Structure  
3. WLM‑Agent‑Behavior — Structure → Behavior  
4. WLM‑Persona‑Engine — Structure → Identity  
5. WLM‑Knowledge‑Engine — Structure → Knowledge  
6. **WLM‑Metacognition‑Engine — Structure → Self‑Monitoring**

It provides the missing link between **reasoning** and **reasoning about reasoning**:

> **Structure → Reasoning → Self‑Monitoring → Stability**

---

## Why this exists

LLMs generate answers, but they do not:

- track their reasoning path  
- detect contradictions  
- maintain dimensional consistency  
- monitor context shifts  
- regulate their own inference process  
- detect when they are hallucinating  

The WLM‑Metacognition‑Engine introduces:

- structured reasoning paths  
- consistency checks  
- dimension‑aware reasoning  
- self‑evaluation signals  
- reasoning‑state transitions  

This is the layer that makes AI **transparent, controllable, and stable**.

---

## What this engine does

Given a reasoning explanation or chain, it produces:

- **steps** — normalized reasoning units  
- **consistency** — contradictions or invalid transitions  
- **dimensions** — which reasoning dimensions are active  
- **signals** — metacognitive indicators  
- **metacognitive graph** — structured representation of the reasoning process  

The output is a deterministic **MetacognitionGraph** object.

---

## Architecture

```
Reasoning Text
    ↓
Reasoning Extractor
    ↓
Consistency Engine
    ↓
Dimension Tracker
    ↓
Signal Engine
    ↓
Metacognition Graph Builder
    ↓
MetacognitionGraph
```

Each module is isolated, testable, and extensible.

---

## Design principles

- **Deterministic** — same reasoning → same metacognition  
- **Interpretable** — explicit steps and signals  
- **Modular** — each engine evolves independently  
- **Dimension‑aligned** — grounded in spatial/temporal/causal/identity/knowledge reasoning  
- **Expandable** — supports richer metacognitive semantics in future phases  

---

## Status

MVP architecture complete.  
Reasoning‑path extraction and contradiction detection planned for Phase 2.

See `docs/roadmap.md` for upcoming milestones.
