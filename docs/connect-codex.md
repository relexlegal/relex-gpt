# Connect Relex to OpenAI Codex

Point Codex at the hosted Relex MCP server:

```
https://relex.legal/api/mcp
```

## OAuth (preferred when the host supports it)

Add an HTTP MCP server named `relex` with that URL. On first tool use, complete
the browser sign-in to Relex.

## API key (CI / headless)

1. Relex → **Settings → API Keys → Create key**.
2. Configure Codex MCP with header:

```
Authorization: Bearer rlx_...
```

Example shape (adapt to your Codex config file):

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

## Skills

Load `plugin/skills/relex/SKILL.md` (and related skills) into the Codex project
or plugin context so the model follows the PII-safe deep-link workflow.

## After connect

Say: *“Set up my practice workflow with Relex.”*
