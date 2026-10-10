# Sprint 1 Retrospective

## What went well

- Small commits made it easy to find what broke the pipeline.
- Tests caught real bugs before I pushed (email validation, blank names).
- The pipeline runs fast (under a minute), so feedback is quick.

## What went badly

1. The first three CI runs all failed. The reason: pytest could not
   import the `app` package on the runner, because the repo root is not
   on `sys.path` there like it is with `python -m pytest` on my machine.
2. The smoke test failed on the CI branch because `app/main.py` was still
   empty there — the FastAPI app was only scaffolded in a later story.
3. When something failed, I had no visibility: no health check and no
   request logs, so I had to guess what the service was doing.

## Improvements for Sprint 2

1. Fixed the CI import problem with `pyproject.toml` (`pythonpath = ["."]`)
   and made the pytest config layout-agnostic; I now run the exact CI
   command locally before pushing.
2. Scaffold the application in the same story as its smoke test
   (done: `chore: scaffold FastAPI application (AGILE-8)`).
3. Add observability: a `GET /health` endpoint plus a console log line
   in every endpoint (planned as AGILE-15 in Sprint 2).
