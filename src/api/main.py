from fastapi import FastAPI
from src.validation.regression_check import validate_routes

app = FastAPI(title="NavGuard Validation API")

@app.get("/validate")
def validate():
    report = validate_routes(
        "data/raw/routes_v1.csv",
        "data/raw/routes_v2.csv"
    )

    failures = [r for r in report if r["status"] == "FAIL"]

    return {
        "status": "FAIL" if failures else "PASS",
        "details": report
    }
