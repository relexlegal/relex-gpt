# Install Relex for ChatGPT and Codex

Relex lets you use ChatGPT / Codex end-to-end on legal matters **without ever
exposing client PII**. Connect once over MCP, sign in in the browser, and set up
your practice workflow.

**MCP URL (everyone):**

```
https://relex.legal/api/mcp
```

## Step 0 — Which subscription?

| Plan | Who adds the connector | Who connects (OAuth) |
|------|------------------------|----------------------|
| **Plus / Pro** (personal) | You | You |
| **Business / Team** | Workspace **owner or admin** | Each **member** |
| **Enterprise / Edu** | Workspace **owner or admin** (apps often disabled by default until enabled) | Each **member** |

If you are not an admin on a managed workspace, skip to
[Member: connect an admin-installed connector](#member-connect-an-admin-installed-connector).

## Personal: Plus / Pro

1. Open ChatGPT → profile menu → **Settings**.
2. Open **Apps** (or **Connectors**).
3. Turn on **Developer mode** / allow custom connectors if shown.
4. **Create** or **Add custom connector** (MCP):
   - Name: `Relex`
   - MCP server URL: `https://relex.legal/api/mcp`
   - Leave OAuth client id/secret blank unless Relex support told you otherwise
     (dynamic OAuth discovery is preferred).
5. Save.
6. Click **Connect** and complete the Relex browser sign-in (Google or Apple).
7. Start a chat, enable the Relex app/connector in the tools panel, and say:

   > Set up my practice workflow with Relex

## Admin: install for the workspace (Business / Team / Enterprise / Edu)

1. Sign in as a **workspace owner or admin**.
2. Open **Workspace settings → Apps** (and **Plugins** if your workspace has it).
3. Confirm that **custom connectors / custom MCP apps / developer mode** are
   allowed for the roles that need Relex. On Enterprise/Edu, apps may be
   **disabled by default** — enable carefully.
4. **Add custom connector**:
   - Name: `Relex`
   - Server URL: `https://relex.legal/api/mcp`
5. **Publish / enable** for the groups or roles that should see it.
6. Tell members: *“Relex is available under Settings → Apps — click Connect and
   sign into your Relex account.”*

Admins do **not** need to share API keys. Each member uses OAuth with their own
Relex account (or a shared firm account if that is your policy — not recommended
for personal PII passwords).

## Member: connect an admin-installed connector

1. Confirm your admin has published Relex.
2. Open **Settings → Apps / Connectors**.
3. Find **Relex** under available / workspace apps.
4. Click **Connect** → browser OAuth to Relex.
5. In chat, enable Relex and say *“Set up my practice workflow with Relex”*.

### If you don't see Relex

| Symptom | Cause | Fix |
|---------|--------|-----|
| No Relex in the list | Admin never added/published it | Ask admin |
| Greyed out / Disabled by admin | App policy or role restriction | Ask admin to enable for your role |
| Connect fails | Network, popup blocked, or wrong Relex account | Allow popups; retry; use correct Google/Apple identity |
| Tools missing | Connector connected but not enabled in the chat | Enable Relex in the chat tools / apps panel |

## Codex

See [connect-codex.md](connect-codex.md). Endpoint is the same MCP URL. Prefer
OAuth when the Codex host supports it; otherwise use a Relex API key as bearer
token for CI.

## After connect — what to expect

1. **PII password** — set in the browser (deep link). Encrypts client identities.
2. **Know-how** — upload playbooks/templates in Relex.
3. **Encrypted parties** — auto-created in the browser; ChatGPT only sees counts.
4. **First case** — agent can open and steer cases; parties/docs/payments stay
   on deep links.

## API-key fallback

Relex → **Settings → API Keys → Create key**, then:

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

Revoke under the same settings page.

## Skills in this package

`plugin/skills/` teach ChatGPT the PII-safe Relex workflow (steering, ontology,
citations, intake, jurisdictions). Load them as plugin skills or system context
when your host supports skill packages. Primary: `plugin/skills/relex/SKILL.md`.
