# Sprint 2 Review

Sprint goal: grow the catalog and make the service observable.

## What I delivered (7 points)

- AGILE-10 – Add shoe (3 pts): `POST /shoes` returns 201 with id, brand,
  model and price; blank brand/model and bad price return 422.
- AGILE-11 – Browse shoes (2 pts): `GET /shoes` returns all added shoes
  in order; empty catalog returns [].
- AGILE-15 – Health endpoint (2 pts): `GET /health` returns 200
  `{"status": "ok"}`; every endpoint prints one console log line
  per request.

## Demo

```
POST /shoes  {"brand": "Nike", "model": "Air Zoom", "price": 120.0}
-> 201  {"id": 1, "brand": "Nike", "model": "Air Zoom", "price": 120.0}

GET /shoes
-> 200  [{"id": 1, "brand": "Nike", ...}, ...]

GET /health
-> 200  {"status": "ok"}

console:  POST /shoes brand=Nike model=Air Zoom price=120.0
console:  GET /shoes
console:  GET /health
```

## Tests

11 tests pass (`pytest --cov=app`, 100% coverage on app code):
1 smoke + 4 merchant + 5 shoe + 1 health test.

## Against the plan and Sprint 1 retro

Sprint 2 planned AGILE-10 + AGILE-11 + AGILE-15 = 7 points, delivered 7.
All three retro improvements from Sprint 1 were applied:
1. ran the exact CI command locally before every push — CI green first
   try on all three branches (runs #13, #14, #15);
2. scaffold lives with its smoke test, no empty-app failures;
3. health endpoint + console logs added (AGILE-15).
