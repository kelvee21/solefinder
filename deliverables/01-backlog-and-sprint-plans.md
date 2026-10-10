# SoleFinder – Backlog & Sprint Plans (Sprint 0)

## Product vision

SoleFinder helps small shoe merchants sell online: merchants register and list
their shoes, and customers can browse the catalog and search by brand.

## Product backlog

Points are relative (merchant registration = 5 points). Highest priority first.

| Key | Story | Epic | Priority | Points | Sprint |
|-----|-------|------|----------|--------|--------|
| AGILE-8 | Set up CI pipeline with GitHub Actions | Platform & Operations | Highest | 2 | Sprint 1 |
| AGILE-9 | As a merchant, I can register so I can sell shoes | Merchant Management | Highest | 5 | Sprint 1 |
| AGILE-10 | As a merchant, I can add a shoe to my inventory | Merchant Management | Highest | 3 | Sprint 2 |
| AGILE-11 | As a customer, I can browse all shoes | Customer Experience | High | 2 | Sprint 2 |
| AGILE-12 | As a customer, I can search shoes by brand | Customer Experience | High | 2 | Backlog |
| AGILE-13 | As a merchant, I can update stock/price or delete a shoe | Merchant Management | Medium | 5 | Backlog |
| AGILE-14 | As a customer, I can register | Customer Experience | Medium | 3 | Backlog |
| AGILE-15 | As an operator, I can check a health endpoint | Platform & Operations | Medium | 2 | Sprint 2 |
| AGILE-16 | As a customer, I can add shoes to a cart | Customer Experience | Low | 5 | Backlog |
| AGILE-17 | As a customer, I can find similar shoes by image (simulated) | Future Ideas (Icebox) | Low | 8 | Backlog |

## Acceptance criteria

- AGILE-8: every push runs the pipeline; install + tests pass on a clean runner.
- AGILE-9: POST /merchants returns 201 with id, name and email; bad email
  and blank name return 422.
- AGILE-10: POST /shoes returns 201 with id, brand, model and price; blank
  brand/model and non-positive price return 422.
- AGILE-11: GET /shoes returns all added shoes; empty catalog returns [].
- AGILE-12: GET /shoes?brand=... returns only matching shoes (future).
- AGILE-13: merchant can change price/stock or delete a shoe (future).
- AGILE-14: POST /customers returns 201; bad data returns 422 (future).
- AGILE-15: GET /health returns 200 {"status": "ok"}; each endpoint prints
  a console log line per request.
- AGILE-16 / AGILE-17: future, criteria to be refined before planning.

## Definition of Done

1. Code merged to the sprint branch and acceptance criteria met.
2. Unit/integration tests written and passing (`pytest`).
3. CI pipeline green on the pushed branch.
4. No junk files committed (`__pycache__`, `.coverage`, secrets).
5. Jira story moved to Done with test/CI evidence linked.

## Sprint 1 plan

Goal: prove we can deliver tested code with CI on every push.
Selected: AGILE-8 (2 pts) + AGILE-9 (5 pts) = 7 points.
I picked the CI task first so every later story is tested automatically.

## Sprint 2 plan

Goal: grow the catalog and make the service observable.
Selected: AGILE-10 (3 pts) + AGILE-11 (2 pts) + AGILE-15 (2 pts) = 7 points.
AGILE-15 is pulled ahead of AGILE-12/13/14 because this sprint requires
monitoring/logging (health endpoint + console logs).
