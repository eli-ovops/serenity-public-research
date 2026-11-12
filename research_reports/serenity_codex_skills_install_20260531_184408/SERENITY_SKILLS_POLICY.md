# Serenity Skills Policy

Generated: 2026-05-31T10:44:53Z
Project: `/Users/USER/Documents/serenity`

## Mode

Serenity Alpha Research is research-only. Skills may support local workflow, public-material research framing, review, debugging, and documentation. Skills must not convert research output into trading instructions.

## Hard Prohibitions

- No buy recommendation.
- No sell recommendation.
- No target price.
- No position sizing.
- No entry point or trade plan.
- No brokerage access.
- No `.env`, API key, secret, token, cookie, SSH key, auth, provider, session, or history reads.
- No scheduler, cron, timer, service, monitor, or automation creation.
- No `git push`.
- No upload of project content to remote systems.
- No system shell profile modification.

## Allowed Skills

- `using-superpowers`: installed by project-level symlink. It must remain subordinate to this Serenity policy and research-only boundaries.
- `brainstorming`: allowed only if locally installed later; use for thesis framing, industry mapping, and red-team questions. Brainstorming output is not evidence.
- `smart-search`: allowed only if locally installed later; use only for public-material research. It must not output buy/sell recommendations, target prices, position sizing, entry points, brokerage actions, paid-wall bypasses, or credential reads.
- `systematic-debugging`: allowed only if locally installed later for local engineering/debug workflow.
- `test-driven-development`: allowed only if locally installed later for local engineering changes.
- `code-review` or `requesting-code-review`: choose one only if locally installed later.
- `decision-log`: allowed only if locally installed later for local decision records.
- `prompt-harness`: allowed only if locally installed later for local prompt testing.
- `using-git-worktrees`: allowed only if locally installed later for local git isolation; no push.

## Forbidden Or Default-Disabled Skills

- `git-pushing`: forbidden by default because Serenity prohibits `git push`.
- `x-twitter-scatter`: not installed; may only be considered after separate authorization as a social-noise public source, not core evidence.
- `ui-ux-pro-max`: not relevant to current research-only skills isolation.
- `skill-creator`: not installed without separate authorization to create a new skill.
- `claude-code-terminal-title`: not installed; not needed for project safety or research workflow.
