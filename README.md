# Relex × GPT (ChatGPT / Codex)

**Legal Workspace — One source of truth for any Agent — confidential by design**

Keep legal knowledge, matter context and saved progress in Relex, independently
of the assistant you use. Authorize another compatible agent to continue from
the same stored context, without rebuilding the background in another chat.

## Portable context, with your permission

1. Create or open the matter in Relex and add information through its protected
   intake and document workflows.
2. Connect a supported client to `https://relex.legal/api/mcp` and authorize
   your own Relex account. Installing a package does not authorize private data.
3. Ask the agent to read the permitted matter context before working and save
   its conclusions when finished. A second authorized client can then use that
   continuing record.

Portability covers information saved in Relex, not automatic import of private
chat histories or a model's internal memory. Client-side identity encryption,
de-identification and MCP access controls protect the supported workflows;
de-identified legal facts may still be sensitive. Review what you authorize.

## Workspace, SDK and Marketplace

Use **Legal Workspace** for persistent legal context; the **Legal SDK** for
building your firm's or legal department's own platform; and the
**Legal Marketplace** to discover published professional profiles or make an
AI-first law firm discoverable across specialties.

An agent may help find a professional and prepare a reference-only request.
The user must review and approve sharing in Relex. Discovery is not engagement,
a completed conflict check, payment or a guarantee of professional availability.

Client support depends on the host product, plan and administrator settings.
Gemini CLI support does not imply support in every Gemini web experience.
Harvey BYOMCP is a customer-admin connection path, not a claim of Harvey
Connector Library listing or approval. Check the current
[connector guides](https://relex.legal/docs/connectors) and
[portable-context guide](https://relex.legal/guides/portable-legal-context).
## How it works

ChatGPT / Codex connect to the **remote MCP server** at
`https://relex.legal/api/mcp` with eleven MCP tools (matter workflows plus `search` / `execute`) and a
fixed ~1k-token cost. Auth is **browser OAuth 2.1 + PKCE** (Google/Apple) —
**no key to paste**. A static API key works for CI/headless Codex.

Party data is sealed client-side; document content is redacted client-side by
default; `execute` refuses plaintext PII and returns deep links instead.


## MCP tools (remote server)

The hosted connector at `https://relex.legal/api/mcp` exposes **eleven** tools:
`list_matters`, `read_matter_context`, `diagnose_matter_sources`,
`save_matter_work_product`, `correct_matter_ontology`, `conclude_matter_session`,
`find_legal_professionals`, `read_legal_professional`, `prepare_professional_request`,
`search`, and `execute`. Auth is OAuth 2.1 + PKCE; connector scopes are
`relex.cases.read relex.cases.write relex.draft`.

ChatGPT redirect forms: `https://chatgpt.com/connector/oauth/{callback_id}` or the stable `https://chatgpt.com/connector_platform_oauth_redirect` (requires RFC 9207 `iss` in the authorization response, which Relex advertises).

## Official OpenAI names

| Surface | Product calls it |
|---------|------------------|
| ChatGPT | **App** / custom **MCP connector** (Settings → **Apps** or **Apps & Connectors**; often needs **Developer mode**) |
| Directory | **Plugin** (can wrap apps + skills — only if published) |
| Workspace admin | **Apps** (+ **Plugins** policy) |
| Codex | **MCP server** |

Always display name **Relex**, URL `https://relex.legal/api/mcp`.

## Which plan do you have?

### ChatGPT Plus / Pro (personal)

**You** create the app / custom connector:

1. **Settings → Apps** (enable **Developer mode** if shown).
2. **Create** / **Add custom connector** (MCP):
   - **Name:** Relex
   - **Server URL:** `https://relex.legal/api/mcp`
3. **Connect** → browser OAuth to Relex.
4. Enable **Relex** in the chat tools panel, then:
   > Set up my practice workflow with Relex

### ChatGPT Business / Team / Enterprise / Edu

| Role | Steps |
|------|--------|
| **Owner / admin** | **Workspace settings → Apps** (+ **Plugins**). Allow custom MCP / developer apps. Add **Relex** → `https://relex.legal/api/mcp`, **publish / enable** for roles. Members cannot add custom entries themselves. |
| **Member** | **Settings → Apps**. Find **Relex**, **Connect**, OAuth *your* Relex account. |

Admin install only makes Relex **visible**. Each member still OAuths alone.

Full guide: [`docs/install.md`](docs/install.md) ·
[`docs/connect-chatgpt.md`](docs/connect-chatgpt.md) ·
[`docs/connect-codex.md`](docs/connect-codex.md) ·
https://relex.legal/docs/connectors/gpt

## Codex

```bash
# HTTP MCP — OAuth when supported; otherwise API key
# Config shape varies by Codex CLI version; endpoint is always:
# https://relex.legal/api/mcp
```

API-key fallback (Relex → **Settings → API Keys**):

```json
{
  "mcpServers": {
    "relex": {
      "url": "https://relex.legal/api/mcp",
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

## Docs on relex.legal

- [GPT connector](https://relex.legal/docs/connectors/gpt)
- [MCP Server](https://relex.legal/docs/mcp)
- [For AI Agents](https://relex.legal/for-agents)

## License

AGPL-3.0-or-later — see [LICENSE](LICENSE).
