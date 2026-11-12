# Rollback Plan

Generated: 2026-05-31T10:44:53Z

## Current Change

The only installed project-level skill is a symlink:

- `/Users/USER/Documents/serenity/.codex/skills/superpowers` -> `/Users/USER/.codex/skills/superpowers`

## Rollback Command

```bash
rm /Users/USER/Documents/serenity/.codex/skills/superpowers
```

## Validation After Rollback

```bash
test ! -e /Users/USER/Documents/serenity/.codex/skills/superpowers
```

## Preinstall Snapshot

See `PREINSTALL_PROJECT_SKILLS_SNAPSHOT.txt` in this report directory.
