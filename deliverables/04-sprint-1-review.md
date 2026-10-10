# Sprint 1 Review

Sprint goal: prove we can deliver tested code with CI on every push.

## What I delivered

- AGILE-8 – CI pipeline (`.github/workflows/ci.yml`): install + `pytest`
  on every push. Branch: `feature/AGILE-8-ci-pipeline`, CI run green.
- AGILE-9 – Merchant registration: `POST /merchants` returns 201 with
  id, name and email; bad email and blank name return 422.
  Branch: `feature/AGILE-9-merchant-registration`, CI run green.

## Demo

```
POST /merchants  {"name": "Foot Locker", "email": "a@shop.com"}
-> 201  {"id": 1, "name": "Foot Locker", "email": "a@shop.com"}

POST /merchants  {"name": "X", "email": "nope"}
-> 422
```

## Tests

5 tests pass (`pytest --cov=app`): 1 smoke test + 4 merchant tests
(register 201, invalid email 422, blank name 422, blank email 422).

## Against the plan

Sprint 1 planned AGILE-8 (2 pts) + AGILE-9 (5 pts) = 7 points.
Delivered 7 points. Nothing spilled over.
