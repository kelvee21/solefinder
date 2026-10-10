# CI/CD Evidence

Pipeline: `.github/workflows/ci.yml` — runs on every push and pull request.
Steps: checkout, set up Python 3.12, `pip install -r requirements.txt`,
`python -m pytest --cov=app --cov-report=term`.

## Sprint 1 runs (both green)

- Run #10, branch `feature/AGILE-8-ci-pipeline` (commit `f877861`): success
  https://github.com/kelvee21/solefinder/actions/runs/38067675736
- Run #11, branch `feature/AGILE-9-merchant-registration` (commit `faae11b`):
  success
  https://github.com/kelvee21/solefinder/actions/runs/38067676495

(Earlier runs #1–#3 failed while I fixed the pytest import path and the
empty `app/main.py` — see the Sprint 1 retrospective.)

## Sprint 2 runs (all green, first try)

- Run #13, branch `feature/AGILE-10-add-shoe`: success
  https://github.com/kelvee21/solefinder/actions/runs/38070007077
- Run #14, branch `feature/AGILE-11-browse-shoes`: success
  https://github.com/kelvee21/solefinder/actions/runs/38070139437
- Run #15, branch `feature/AGILE-15-health-endpoint`: success
  https://github.com/kelvee21/solefinder/actions/runs/38070254452

Every Sprint 2 run shows all steps successful: checkout, setup-python,
pip install, pytest with coverage, post steps. The pytest step output also
shows the console request logs, e.g. `POST /shoes brand=Nike ...`,
`GET /shoes`, `GET /health`.
