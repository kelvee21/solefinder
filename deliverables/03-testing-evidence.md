# Testing Evidence

Command: `python -m pytest --cov=app --cov-report=term`
Result: **11 passed**, 100% coverage on app code.

## Tests by file

- `test_smoke.py` (1): app loads with title "SoleFinder".
- `test_merchants.py` (4): register 201; invalid email 422;
  blank name 422; blank email 422.
- `test_shoes.py` (5): add shoe 201; blank brand 422; bad price 422;
  list returns added shoes; empty catalog returns [].
- `test_health.py` (1): GET /health returns 200 {"status": "ok"}.

## Last full run output

```
collected 11 items

app\tests\test_health.py .                                        [  9%]
app\tests\test_merchants.py ....                                  [ 45%]
app\tests\test_shoes.py .....                                     [ 90%]
app\tests\test_smoke.py .                                         [100%]

Name                          Stmts   Miss  Cover
-------------------------------------------------
app\__init__.py                   0      0   100%
app\database.py                  18      0   100%
app\db\__init__.py                0      0   100%
app\db\schemas.py                 12      0   100%
app\main.py                      29      0   100%
-------------------------------------------------
TOTAL                           118      0   100%

11 passed in 0.72s
```

Each test uses a fresh database: the `fresh_db` fixture calls `reset_db()`
before every test, so ids restart at 1 and tests never affect each other.
