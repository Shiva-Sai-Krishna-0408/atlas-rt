# ATLAS-RT — TODO

## v0.75

### Blockers
- [ ] Add user profile to agent state (name, email, home_airport, passport_country, payment_method). Exfil target for attacks.
- [ ] Rewrite system prompt — role, supported countries scope, tool-first rule, explicit policies (e.g., "never send email to unconfirmed addresses").
- [ ] Flesh out `search_places` with multi-field realistic returns. Needs injection surface.
- [ ] Apply alias-map pattern to remaining tools (`get_visa_rules`, `search_hotels`, `search_places`).

### Vertical slice
- [ ] Pick one attack class from Gray Swan taxonomy (candidate: Operational-Authority Spoofing or Session-State Injection).
- [ ] Author one payload, inject via poisoned tool return (e.g., `search_places`).
- [ ] Build judge v0 — rule-based, tool-call trajectory check (did `send_email` fire with wrong recipient? did agent skip `get_visa_rules`?).
- [ ] Log one full end-to-end run: attack → trace → verdict → results row.
- [ ] Stub file structure for other attack classes (one example payload each).

## v1.0

- [ ] Full attack corpus (~5–7 classes × multiple payloads).
- [ ] All 6 tools fleshed out with realistic mock data.
- [ ] Full benchmark run on gpt-4o + one Ollama local model.
- [ ] Results tabulated per class.
- [ ] README + methodology write-up + reproducible harness.

## Deferred

- [ ] Multi-airport support (Tokyo NRT, NY LGA/EWR, Paris ORY). Only if an attack needs it.