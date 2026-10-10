# Sprint 2 Retrospective

## What went well

- CI was green on the first try for every Sprint 2 branch — the Sprint 1
  lesson (run the exact CI command locally) worked.
- Small commits (schema, then schemas, then endpoint, then tests) made
  each step easy to check.
- The `reset_db` test fixture from Sprint 1 worked unchanged for shoes.

## What went badly

1. Adding console logs meant editing every endpoint function by hand —
   repetitive. Next time I would look for one central place for logging.
2. I first wrote the pytest config with only `app/tests`, which broke CI
   on the older branch layout (`tests/`). Fixed by keeping the config
   layout-agnostic.
3. My first CI runs in Sprint 1 failed because I only ran
   `python -m pytest` locally, which hides import problems.

## Lessons and improvements

- Keep stories small and in one pattern (table, schemas, endpoint,
  tests) — it made Sprint 2 predictable.
- Request logs already helped: I can see every call in the console.
- Next: AGILE-12 (search by brand), then AGILE-13 (update/delete shoe).
