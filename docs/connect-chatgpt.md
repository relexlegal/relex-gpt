# Connect Relex to ChatGPT

Use Relex as a **custom MCP connector / app** in ChatGPT. Sign-in is a
**browser OAuth flow** — no key to paste.

## Personal (Plus / Pro)

1. **Settings → Apps** (or **Connectors**).
2. Enable developer / custom connector creation if required.
3. **Add custom connector**:
   - Name: `Relex`
   - URL: `https://relex.legal/api/mcp`
4. **Connect** → sign in to Relex.
5. In a new chat, enable Relex, then: *“Set up my practice workflow with Relex”*.

## Team / Business / Enterprise / Edu

### Admin (once)

1. **Workspace settings → Apps** (+ **Plugins** if present).
2. Allow custom MCP connectors for the right roles.
3. Add **Relex** → `https://relex.legal/api/mcp`.
4. Publish / enable for members.

### Member (each person)

1. **Settings → Apps / Connectors**.
2. Select **Relex** (already listed — you cannot add it yourself).
3. **Connect** → OAuth.
4. Enable in chat and start working.

Members who try to “Add custom connector” and fail are usually on a managed plan
where only admins can install. That is expected.

## Using Relex in conversation

Ask: “Start a Relex case for me” or “Help me draft on my Relex case.”

ChatGPT works on structure and drafting. For client personal data, documents,
payment, or export it will give you a secure Relex deep link — open it in the
browser.

## Fallback — API key

Settings → API Keys in Relex, then pass
`Authorization: Bearer rlx_...` if your ChatGPT/custom app UI supports headers.
OAuth remains preferred.
