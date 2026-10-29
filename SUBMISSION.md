# Submission — OpenAI Plugins (ChatGPT + Codex)

> Prepared 2026-10-28; updated the same day for MCP server version 1.1.0
> (branch `docs/read-api-1.1.0`). Nothing has been submitted. The backend with
> neutral server instructions, data-only responses and the `read_api` tool is
> on `master` (5a5d7b9) and deployed as revision `relex-backend-00192`.

Hosted server: `https://relex.legal/api/mcp` (streamable HTTP, OAuth 2.1 with
PKCE and dynamic client registration). Thirteen tools: `list_matters`,
`read_matter_context`, `diagnose_matter_sources`, `read_matter_source`,
`save_matter_work_product`, `correct_matter_ontology`, `conclude_matter_session`,
`find_legal_professionals`, `read_legal_professional`,
`prepare_professional_request`, `search`, `read_api`, `execute`.

Server version 1.1.0. `read_api` reads one GET endpoint (read-only; parameters
`path` and optional `query`). `execute` creates, updates or deletes through one
endpoint (POST/PUT/PATCH/DELETE); DELETE and other irreversible routes are not
applied by the tool and return a Relex deep link where the user confirms the
change.

Requirements checked 2026-10-28 against developers.openai.com/plugins/deploy/
(submission, app-review, submission-errors).

## Done in this branch
- [x] `plugin/plugin.json` uses the portable Agent Plugins schema with `extensions.com.openai`: interface (displayName "Relex Legal", shortDescription "Legal practice management" — both ≤30 chars; longDescription; category "Business & Operations"; capabilities; website/support/privacy/terms URLs; logo + composer icon; 3 starter prompts ≤128 chars), onboardingSkill, review (exactly 5 positive + 3 negative test cases, commerce=false with explanation) and release notes. Version 0.1.10.
- [x] `plugin/mcp.json` (portable, `streamable-http`, no client secret); `.mcp.json` kept for Codex.
- [x] `scripts/build_openai_zip.py` builds `dist/relex-legal-openai.zip`: plugin root only, excludes `commands/`, `agents/`, `.grok-plugin/` (not loaded by ChatGPT), and adds a `SKILL.md` to `skills/jurisdictions/` inside the ZIP (the portal requires one in every `skills/*` folder).
- [x] No hooks, no `apps/` / `.app.json`, no credentials in the package.
- [x] Every server tool already has explicit `readOnlyHint`, `openWorldHint`, `destructiveHint`.

## User must do
- [ ] Check the live server before the tool scan (it reads the live server and rescans daily after publication): `tools/list` returns the thirteen tools with the annotations below.
- [ ] Verify an individual or business identity in the OpenAI Platform dashboard.
- [ ] Domain verification: publish the token the portal gives you as plain text at `https://relex.legal/.well-known/openai-apps-challenge` (frontend/hosting change, not made here).
- [ ] Reviewer account: OpenAI rejects MFA, email/SMS codes and magic links. Relex sign-in is Google/Apple plus an email **link** (`signInWithEmailLink` in `frontend/src/lib/services/authService.ts`); there is no password login. Create a dedicated Google account without 2-step verification, give it the QA matter (synthetic data only), and enter it in the portal — or add a reviewer password login. [CONFIRM WITH GEORGE]
- [ ] Record the demo video (all five positive cases on ChatGPT web + Codex) and paste its URL as `demo_recording_url` in the portal.
- [ ] Write a one-sentence justification per annotation per tool in the portal (suggested wording below).
- [ ] Confirm `commerce=false` is correct: payments for case tiers / professional fees happen only in the Relex web app.
- [ ] `python3 scripts/build_openai_zip.py`, upload the ZIP (With MCP → `https://relex.legal/api/mcp`), run the tool scan, attest the policies, submit.

## Annotation justifications (suggested)
Values match the server's tool annotations (server version 1.1.0).

| Tool | readOnly | openWorld | destructive | idempotent | Justification |
|---|---|---|---|---|---|
| list_matters, read_matter_context, diagnose_matter_sources, read_matter_source, find_legal_professionals, read_legal_professional, search, read_api | true | false | false | true | Reads data from the user's own Relex account or the published Marketplace; changes nothing. `read_api` accepts GET endpoints only. |
| save_matter_work_product, correct_matter_ontology | false | false | true | true | Writes a new revision inside the user's matter; revision-checked, so the same call against the same base revision is not applied twice. Marked destructive because the new revision supersedes the current one; earlier revisions remain. |
| prepare_professional_request | false | false | false | true | Creates a pending request in Relex; nothing is sent, shared or charged until the user approves it in Relex. |
| conclude_matter_session | false | false | false | false | Saves the session's distilled conclusions to the matter thread as a new entry; nothing is overwritten. Each call adds an entry. |
| execute | false | false | true | false | Creates, updates or deletes data through one documented Relex API endpoint (POST/PUT/PATCH/DELETE). DELETE and other irreversible routes are not applied by the tool; they return a Relex deep link where the user confirms the change. |
