# Submission — OpenAI Plugins (ChatGPT + Codex)

> Prepared 2026-10-28 on branch `directory-review-2026-10`. Nothing has been
> submitted, pushed or deployed. Before any submission: deploy the backend branch
> `directory-review-2026-10` (neutral server instructions, data-only responses),
> then merge and push this repo.

Hosted server: `https://relex.legal/api/mcp` (streamable HTTP, OAuth 2.1 with
PKCE and dynamic client registration). Twelve tools: `list_matters`,
`read_matter_context`, `diagnose_matter_sources`, `read_matter_source`,
`save_matter_work_product`, `correct_matter_ontology`, `conclude_matter_session`,
`find_legal_professionals`, `read_legal_professional`,
`prepare_professional_request`, `search`, `execute`.

Requirements checked 2026-10-28 against developers.openai.com/plugins/deploy/
(submission, app-review, submission-errors).

## Done in this branch
- [x] `plugin/plugin.json` uses the portable Agent Plugins schema with `extensions.com.openai`: interface (displayName "Relex Legal", shortDescription "Legal practice management" — both ≤30 chars; longDescription; category "Business & Operations"; capabilities; website/support/privacy/terms URLs; logo + composer icon; 3 starter prompts ≤128 chars), onboardingSkill, review (exactly 5 positive + 3 negative test cases, commerce=false with explanation) and release notes. Version 0.1.8.
- [x] `plugin/mcp.json` (portable, `streamable-http`, no client secret); `.mcp.json` kept for Codex.
- [x] `scripts/build_openai_zip.py` builds `dist/relex-legal-openai.zip`: plugin root only, excludes `commands/`, `agents/`, `.grok-plugin/` (not loaded by ChatGPT), and adds a `SKILL.md` to `skills/jurisdictions/` inside the ZIP (the portal requires one in every `skills/*` folder).
- [x] No hooks, no `apps/` / `.app.json`, no credentials in the package.
- [x] Every server tool already has explicit `readOnlyHint`, `openWorldHint`, `destructiveHint`.

## User must do
- [ ] Deploy the backend branch first (the tool scan reads the live server; it rescans daily after publication).
- [ ] Verify an individual or business identity in the OpenAI Platform dashboard.
- [ ] Domain verification: publish the token the portal gives you as plain text at `https://relex.legal/.well-known/openai-apps-challenge` (frontend/hosting change, not made here).
- [ ] Reviewer account: OpenAI rejects MFA, email/SMS codes and magic links. Relex sign-in is Google/Apple plus an email **link** (`signInWithEmailLink` in `frontend/src/lib/services/authService.ts`); there is no password login. Create a dedicated Google account without 2-step verification, give it the QA matter (synthetic data only), and enter it in the portal — or add a reviewer password login. [CONFIRM WITH GEORGE]
- [ ] Record the demo video (all five positive cases on ChatGPT web + Codex) and paste its URL as `demo_recording_url` in the portal.
- [ ] Write a one-sentence justification per annotation per tool in the portal (suggested wording below).
- [ ] Confirm `commerce=false` is correct: payments for case tiers / professional fees happen only in the Relex web app.
- [ ] `python3 scripts/build_openai_zip.py`, upload the ZIP (With MCP → `https://relex.legal/api/mcp`), run the tool scan, attest the policies, submit.

## Annotation justifications (suggested)
| Tool | readOnly | openWorld | destructive | Justification |
|---|---|---|---|---|
| list_matters, read_matter_context, diagnose_matter_sources, read_matter_source, find_legal_professionals, read_legal_professional, search | true | false | false | Reads data from the user's own Relex account or the published Marketplace; changes nothing. |
| save_matter_work_product, correct_matter_ontology | false | false | false | Writes a new revision inside the user's matter; revision-checked, earlier revisions remain. |
| prepare_professional_request | false | false | false | Creates a pending request in Relex; nothing is sent, shared or charged until the user approves it in Relex. |
| conclude_matter_session | false | true | false | Saves the session's distilled conclusions to the matter thread (new entry, nothing overwritten); may use model processing, and saved work products are visible to every connected host. |
| execute | false | true | true | Generic call to one documented Relex API endpoint (GET/POST/PATCH/DELETE), so it can update or delete matter data. |
