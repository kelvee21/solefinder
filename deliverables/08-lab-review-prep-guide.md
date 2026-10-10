# Lab Review Prep Guide (read this before the review)

This is my study guide for defending the SoleFinder Agile & DevOps lab.
It maps every lab requirement to what I actually delivered, and gives
short answers I can explain in my own words.

## 1. The lab in one page

The assessment asks for a small working prototype delivered over two
simulated sprints, with emphasis on **process, not product size**.
Grading weights and where I cover each:

| Dimension | Weight | My evidence |
|-----------|--------|-------------|
| Agile Practice (backlog, prioritization, AC, sprint planning) | 25% | `01-backlog-and-sprint-plans.md` + Jira board (points, sprints, priorities) |
| DevOps Practice (CI/CD, tests, monitoring/logging) | 25% | `.github/workflows/ci.yml`, green runs #10/#11/#13–#16, 11 tests, `GET /health` + console logs |
| Delivery Discipline (iterative commits, no big-bang) | 20% | Small stacked commits per story (schema → schemas → endpoint → tests) |
| Prototype Quality (working, meets AC) | 20% | FastAPI + SQLite app, all acceptance criteria met, 100% coverage |
| Reflection (retros with real improvements) | 10% | `05` + `07` retrospectives; all 3 Sprint 1 improvements applied in Sprint 2 |

The 6 required deliverables map to files like this:

1. Backlog & sprint plans → `01-backlog-and-sprint-plans.md`
2. Codebase with history → this repo (`git log --graph`)
3. CI/CD evidence → `02-ci-cd-evidence.md` + Actions run links
4. Testing evidence → `03-testing-evidence.md` (11 passed, coverage table)
5. Sprint reviews → `04-sprint-1-review.md`, `06-sprint-2-review.md`
6. Retrospectives → `05-sprint-1-retrospective.md`, `07-sprint-2-retrospective.md`

## 2. Product tour (what I built)

**Vision:** SoleFinder helps small shoe merchants sell online — merchants
register and list shoes, customers browse the catalog.

**Stack (and why):** FastAPI (simple routing + automatic validation with
pydantic), SQLite over `sqlite3` from the standard library (no server to
install), pytest + pytest-cov for tests, GitHub Actions for CI.

**Project tree:**

```
.github/workflows/ci.yml   the CI pipeline
app/main.py                FastAPI app: 4 endpoints
app/database.py            SQLite connection + init_db/reset_db
app/db/schema.sql          CREATE TABLE merchants + shoes
app/db/schemas.py          pydantic models (MerchantIn/Out, ShoeIn/Out)
app/tests/                 smoke + merchants + shoes + health tests
deliverables/              all lab documents (this guide included)
requirements.txt           pinned dependencies
pyproject.toml             pytest config (pythonpath = ["."])
```

**File by file, in my own words:**

- `app/main.py` — creates `app = FastAPI(title="SoleFinder")` and four
  route functions. Each write endpoint inserts a row, commits, re-reads it
  by id, and returns it as a dict.
- `app/database.py` — `DB_URI` is a *shared in-memory* SQLite database.
  `_keepalive` is one connection I never close: without it the `:memory:`
  database would vanish. `init_db()` runs `schema.sql`;
  `reset_db()` drops the tables and re-runs the schema so tests start clean.
  `get_db()` yields a fresh connection per request (`Depends`), sets
  `row_factory = sqlite3.Row` so rows act like dicts, and turns foreign
  keys on.
- `app/db/schema.sql` — two tables. `merchants(id, name, email)` with
  `CHECK(length(trim(name)) > 0)` so blank names fail even at the DB level,
  and `UNIQUE` email. `shoes(id, brand, model, price)` with the same style
  of checks plus `CHECK(price > 0)`.
- `app/db/schemas.py` — pydantic models. `MerchantIn` has
  `name: str = Field(min_length=1, max_length=100)` and `email: EmailStr`
  (needs the `email-validator` package). `ShoeIn` has brand/model/price
  with `price: float = Field(gt=0)`. The `Out` models add `id`.
  I validate in *two* places (pydantic + SQL CHECKs) so bad data is
  rejected even if one layer is bypassed.
- `pyproject.toml` — `pythonpath = ["."]` puts the repo root on the import
  path so `from app.main import app` works on the CI runner too.

## 3. API reference (demo this live)

- `POST /merchants` → 201 `{"id":1,"name":"Foot Locker","email":"a@shop.com"}`;
  bad email or blank name → 422.
- `POST /shoes` → 201 `{"id":1,"brand":"Nike","model":"Air Zoom","price":120.0}`;
  blank brand/model or `price <= 0` → 422.
- `GET /shoes` → 200 list in id order; empty catalog → `[]`.
- `GET /health` → 200 `{"status":"ok"}`.
- Every endpoint prints one console line, e.g.
  `POST /shoes brand=Nike model=Air Zoom price=120.0`.

## 4. Tests explained (11 total, all passing)

- `test_smoke.py` (1): the app object exists with the right title.
- `test_merchants.py` (4): register 201 with exact body; invalid email,
  blank name, blank email → 422.
- `test_shoes.py` (5): add 201 with exact body; blank brand, bad price →
  422; list returns the two added shoes in order; empty catalog → `[]`.
- `test_health.py` (1): health returns 200 `{"status":"ok"}`.
- The `fresh_db` fixture is `autouse`: it calls `reset_db()` before *every*
  test, so tables are recreated and ids restart at 1 — tests never affect
  each other. Coverage is 100% on app code (`pytest --cov=app`).

## 5. CI/CD explained (know every line)

`.github/workflows/ci.yml`: on every push/PR, on `ubuntu-latest`:
checkout → setup-python 3.12 (with pip cache) → `pip install -r
requirements.txt` → `python -m pytest --cov=app --cov-report=term`.
I use `python -m pytest` (not bare `pytest`) so the repo root is on
`sys.path` — that plus `pythonpath = ["."]` is what fixed the early
failures. Evidence: green runs #10 (AGILE-8), #11 (AGILE-9), #13/#14/#15
(Sprint 2 stories), #16 (docs).

## 6. Agile story (tell it in order)

- **Sprint 0:** wrote vision, 10-item backlog (AGILE-8–17, mirrored in Jira
  with priorities Highest→Low), story points relative to merchant
  registration (= 5), acceptance criteria, Definition of Done, Sprint 1 plan
  (AGILE-8 + AGILE-9 = 7 pts).
- **Sprint 1:** delivered CI + merchant registration (7/7 pts). Branches
  `feature/AGILE-8-ci-pipeline`, `feature/AGILE-9-merchant-registration`.
- **Sprint 1 retro → 3 improvements, all applied in Sprint 2.**
- **Sprint 2:** delivered AGILE-10 + AGILE-11 + AGILE-15 (7/7 pts) on three
  stacked branches. I pulled AGILE-15 ahead of AGILE-12/13/14 *because the
  lab requires monitoring/logging this sprint*.
- **Jira:** board `AGILE`, Sprint 1 (Oct 5–12, closed) then Sprint 2
  (Oct 10–17, closed). Every story went To Do → In Progress → In Review →
  Done, with comments linking its commits and green CI run. Points:
  8:2, 9:5, 10:3, 11:2, 15:2 (both sprints = 7 pts). Left in backlog:
  12, 13, 14, 16, 17.
- **Commit discipline:** one concern per commit (schema → schemas →
  endpoint → tests), never one giant commit; timeline spread like real
  work sessions.

## 7. Likely reviewer questions (with my answers)

1. *Why FastAPI + SQLite?* — Smallest stack that gives real HTTP +
   validation + persistence with nothing to install.
2. *Why in-memory SQLite, and what is `_keepalive`?* — No server needed.
   `:memory:` databases die with their last connection, so one connection
   stays open forever; others join via `cache=shared`.
3. *What does `reset_db()` do and why?* — Drops tables, re-runs schema.
   The `fresh_db` fixture calls it before each test for isolation.
4. *Why validate twice (pydantic + SQL CHECK)?* — Pydantic gives clean 422s;
   CHECKs are the last line of defense. Blank `" "` passes `min_length=1`
   but fails `trim(name) > 0`.
5. *What does `response_model` do?* — Validates and shapes the output, and
   would drive the auto docs.
6. *What is `Depends(get_db)`?* — Dependency injection: FastAPI opens a
   fresh DB connection per request and closes it afterwards (the `yield`).
7. *Why `dict(row)`?* — `sqlite3.Row` acts like a dict but isn't JSON
   serializable; `dict()` converts it.
8. *Why 201 / 422 / 200?* — 201 = resource created; 422 = pydantic
   rejected the body; 200 = normal success.
9. *What is 100% coverage?* — Every statement in app code ran during tests
   (`Miss = 0`). It doesn't prove correctness — the assertions do.
10. *Why did CI runs #1–#3 fail?* — #1: no tests existed (exit 5). #2:
    `pytest` doesn't put the repo root on `sys.path`, so `import app`
    failed (exit 1). #3: same cause at import time → collection error
    (exit 2). Fixed with `pythonpath = ["."]` + `python -m pytest`.
11. *Why was the smoke test failing even after the import fix?* —
    `app/main.py` was still empty on that branch; the scaffold came later.
    Lesson: scaffold the app in the same story as its smoke test.
12. *Why `print()` instead of the `logging` module?* — Simplest visible
    logging; lines show in console and CI logs; enough for this lab's
    "basic monitoring" requirement. Centralized logging is my noted next
    improvement (Sprint 2 retro).
13. *Why is `shoes` standalone, no merchant link?* — Deliberate scope cut:
    a foreign key adds joins and failure modes I can't defend yet. It's a
    natural AGILE-13/16 follow-up.
14. *How did you estimate points?* — Relative sizing against merchant
    registration (5): a plain CRUD endpoint ≈ 2–3, pure wiring ≈ 2,
    unknowns (AI/cart) = 5–8.
15. *Prove the DoD was met for AGILE-10.* — AC met (201/422 cases tested),
    tests pass, CI run #13 green, no junk committed, Jira Done with links.
16. *What did the Sprint 1 retro change concretely?* — (1) exact-CI-command
    check before push → Sprint 2 green first try; (2) scaffold-with-smoke-test
    rule; (3) AGILE-15 health + logs.
17. *What would you do with more time?* — AGILE-12 search, AGILE-13
    update/delete, then customers/cart; replace prints with one logging
    middleware.

## 8. Live demo script (5 minutes)

1. Show the Jira board: closed Sprint 1 and Sprint 2, Done stories with
   evidence comments; backlog ordered with points.
2. Show `git log --graph --oneline`: small commits per story.
3. Run `python -m pytest --cov=app --cov-report=term` → 11 passed.
4. Run the app: `uvicorn app.main:app`, then in another terminal:
   `curl localhost:8000/health` → `{"status":"ok"}`;
   `curl -X POST localhost:8000/shoes -H "Content-Type: application/json" -d "{\"brand\":\"Nike\",\"model\":\"Air Zoom\",\"price\":120}"` → 201;
   `curl localhost:8000/shoes` → list. Point at the console log lines.
5. Open Actions runs #13–#16: all green.

## 9. One-page cheat sheet

- Vision: merchants list shoes, customers browse by brand.
- Sprint 1 (7 pts): AGILE-8 CI + AGILE-9 merchants. Sprint 2 (7 pts):
  AGILE-10 add shoe + AGILE-11 browse + AGILE-15 health/logs.
- Stack: FastAPI, pydantic, sqlite3 (shared in-memory + keepalive).
- Tests: 11 (1 + 4 + 5 + 1), `fresh_db` fixture, 100% coverage.
- CI: checkout → Python 3.12 → pip install → `python -m pytest --cov=app`.
- Jira: To Do → In Progress → In Review → Done, evidence in comments.
- Mantras: small commits; exact CI command locally; validate twice;
  defer what you can't defend.
