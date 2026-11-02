# Model-Agnostic AI

## Purpose

AIOS is designed to be independent of any specific Large Language Model (LLM).

The same governance rules should produce consistent engineering outcomes regardless of the underlying AI model.

This principle ensures that repositories built with AIOS remain portable across different AI platforms.

---

# Core Principle

AIOS defines the rules.

The selected AI model performs the implementation.

Changing the AI model must not change:

- repository structure
- engineering quality expectations
- documentation standards
- writing and review discipline
- AIOS compliance

The AI model is an implementation detail.

AIOS is the governing framework.

---

# Architecture

```
AIOS Governance
        │
        ▼
Prompt
        │
        ▼
Any Compatible LLM
        │
        ▼
Consistent Output
```

The governance layer remains constant.

Only the implementation engine changes.

---

# Supported Models

AIOS is designed to work with any capable Large Language Model, including but not limited to:

- ChatGPT
- Codex
- Claude
- Gemini
- DeepSeek
- Qwen
- Llama
- Mistral
- Grok

Additional models can be adopted without modifying AIOS governance documents.

---

# Model Responsibilities

Regardless of the selected model, AI assistants are expected to:

- follow all AIOS governance documents;
- respect the active operating mode or task scope;
- preserve repository architecture;
- preserve the repository's stated intent and quality bar;
- avoid inventing undocumented conventions.

---

# AIOS Responsibilities

AIOS is responsible for defining:

- governance
- engineering standards
- repository conventions
- documentation expectations
- lifecycle vocabulary where used
- decision policies
- operating guidance for agents

AIOS deliberately avoids model-specific behaviour.

---

# Future Compatibility

Future AI models should require little or no change to AIOS.

Only optional implementation guidance may evolve.

The governance layer should remain stable.
