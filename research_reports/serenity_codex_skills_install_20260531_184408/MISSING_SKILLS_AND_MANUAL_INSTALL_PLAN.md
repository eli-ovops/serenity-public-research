# Missing Skills And Manual Install Plan

Generated: 2026-05-31T10:44:53Z

No network installation was performed. The following recommended Serenity skills were not found in allowed local sources:

- brainstorming
- smart-search
- systematic-debugging
- test-driven-development
- code-review-or-requesting-code-review
- decision-log
- prompt-harness
- using-git-worktrees

Manual next step, only after separate user authorization:

1. Identify an approved local or remote source for each missing skill.
2. Verify the source does not require reading credentials, sessions, history, auth, provider, token, key, secret, cookie, or `.env` material.
3. Install into `/Users/USER/Documents/serenity/.codex/skills/` only.
4. Recreate `SKILL_INSTALL_MANIFEST.csv` and hash inventory.
5. Keep `git-pushing` disabled and install only one of `code-review` or `requesting-code-review`.
