# Security

Relex lets you use ChatGPT / Codex on legal matters **without exposing client
PII to the model**.

## Authentication

- MCP: `https://relex.legal/api/mcp`
- OAuth 2.1 + PKCE (Google/Apple) — no key paste
- API key fallback from Relex **Settings → API Keys**
- Revoke under **Settings → API Keys**; clients under **Settings → Agents**

## Client PII never reaches the model

- Party data sealed client-side under the user's PII password
- Documents redacted client-side by default
- MCP `execute` blocks plaintext party/document endpoints and returns deep links
- Model sees labels like `[Party 1]` and anonymized counts only

## This repository

No secrets ship here. Tool handlers and PII guards run in the Relex backend.

## Reporting

**security@relex.legal** — private disclosure only.
