# Relex × GPT (ChatGPT / Codex)

Let a lawyer's **ChatGPT** or OpenAI **Codex** operate inside a **Relex** legal
case — **without ever receiving PII**.

> Relex doesn't replace ChatGPT. It helps you use it end-to-end by protecting
> your PII data and know-how, automating customer service, handling payments for
> free, and giving you access to a new market. See
> [`docs/positioning.md`](docs/positioning.md).

Downstream of the shared Relex MCP server. Base package:
[relexyou/relex-mcp](https://github.com/relexyou/relex-mcp). Sibling connectors:
[Claude](https://github.com/relexyou/relex-claude) ·
[Grok](https://github.com/relexyou/relex-grok) ·
[Gemini](https://github.com/relexyou/relex-gemini).

## How it works

ChatGPT / Codex connect to the **remote MCP server** at
`https://relex.you/api/mcp` with two tools — `search` and `execute` — and a
fixed ~1k-token cost. Auth is **browser OAuth 2.1 + PKCE** (Google/Apple) —
**no key to paste**. A static API key works for CI/headless Codex.

Party data is sealed client-side; document content is redacted client-side by
default; `execute` refuses plaintext PII and returns deep links instead.

## Official OpenAI names

| Surface | Product calls it |
|---------|------------------|
| ChatGPT | **App** / custom **MCP connector** (Settings → **Apps** or **Apps & Connectors**; often needs **Developer mode**) |
| Directory | **Plugin** (can wrap apps + skills — only if published) |
| Workspace admin | **Apps** (+ **Plugins** policy) |
| Codex | **MCP server** |

Always display name **Relex**, URL `https://relex.you/api/mcp`.

## Which plan do you have?

### ChatGPT Plus / Pro (personal)

**You** create the app / custom connector:

1. **Settings → Apps** (enable **Developer mode** if shown).
2. **Create** / **Add custom connector** (MCP):
   - **Name:** Relex
   - **Server URL:** `https://relex.you/api/mcp`
3. **Connect** → browser OAuth to Relex.
4. Enable **Relex** in the chat tools panel, then:
   > Set up my practice workflow with Relex

### ChatGPT Business / Team / Enterprise / Edu

| Role | Steps |
|------|--------|
| **Owner / admin** | **Workspace settings → Apps** (+ **Plugins**). Allow custom MCP / developer apps. Add **Relex** → `https://relex.you/api/mcp`, **publish / enable** for roles. Members cannot add custom entries themselves. |
| **Member** | **Settings → Apps**. Find **Relex**, **Connect**, OAuth *your* Relex account. |

Admin install only makes Relex **visible**. Each member still OAuths alone.

Full guide: [`docs/install.md`](docs/install.md) ·
[`docs/connect-chatgpt.md`](docs/connect-chatgpt.md) ·
[`docs/connect-codex.md`](docs/connect-codex.md) ·
https://relex.you/docs/connectors/gpt

## Codex

```bash
# HTTP MCP — OAuth when supported; otherwise API key
# Config shape varies by Codex CLI version; endpoint is always:
# https://relex.you/api/mcp
```

API-key fallback (Relex → **Settings → API Keys**):

```json
{
  "mcpServers": {
    "relex": {
      "url": "https://relex.you/api/mcp",
      "headers": {
        "Authorization": "Bearer rlx_..."
      }
    }
  }
}
```

## Layout

```
relex-gpt/
├── plugin/
│   ├── .mcp.json
│   ├── plugin.json
│   ├── skills/           PII-safe workflow skills (ChatGPT-adapted)
│   ├── agents/
│   ├── commands/
│   └── references/
├── docs/
│   ├── install.md
│   ├── connect-chatgpt.md
│   ├── connect-codex.md
│   └── positioning.md
└── SECURITY.md
```

## Docs on relex.you

- [GPT connector](https://relex.you/docs/connectors/gpt)
- [MCP Server](https://relex.you/docs/mcp)
- [For AI Agents](https://relex.you/for-agents)

## License

AGPL-3.0-or-later — see [LICENSE](LICENSE).
