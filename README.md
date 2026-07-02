# ATLAS-RT

**Agentic Travel Layered Adversarial Suite for Red Teaming**

A benchmark for measuring indirect prompt injection against agentic travel-planning systems. Scores model *actions* (tool calls), not outputs.

## Status

Work in progress. Targeting mid-August 2026.

## Structure

    src/atlas_rt/
      clients/   # LLM API wrappers (Anthropic, OpenAI)
      tasks/     # Benchmark task definitions
      attacks/   # Indirect injection payloads
      judge/     # Scoring logic (action-based)
      logging/   # Run logging / trace capture
    data/
      tasks/     # Task specifications (versioned)
      runs/      # Raw run outputs (gitignored)
      results/   # Aggregated results (gitignored)

## Setup

    python -m venv .venv
    source .venv/Scripts/activate  # Windows Git Bash
    pip install -e ".[dev]"

Create a `.env` with:

    ANTHROPIC_API_KEY=...
    OPENAI_API_KEY=...

## License

MIT
