import pandas as pd
from src.metrics.eta_accuracy import eta_error_percentage
from src.metrics.turn_accuracy import turn_accuracy

ETA_THRESHOLD = 0.05  # 5% tolerance

def validate_routes(v1_path: str, v2_path: str):
    v1 = pd.read_csv(v1_path)
    v2 = pd.read_csv(v2_path)

    report = []

    for route_id in v1["route_id"]:
        r1 = v1[v1["route_id"] == route_id].iloc[0]
        r2 = v2[v2["route_id"] == route_id].iloc[0]

        eta_v1 = eta_error_percentage(r1["eta_seconds"], r1["actual_time_seconds"])
        eta_v2 = eta_error_percentage(r2["eta_seconds"], r2["actual_time_seconds"])

        turns_v1 = turn_accuracy(r1["wrong_turns"])
        turns_v2 = turn_accuracy(r2["wrong_turns"])

        status = "PASS"
        issues = []

        if eta_v2 - eta_v1 > ETA_THRESHOLD:
            status = "FAIL"
            issues.append("ETA regression beyond acceptable threshold")


        if turns_v2 > turns_v1:
            status = "FAIL"
            issues.append("Turn accuracy regression")

        report.append({
            "route_id": route_id,
            "status": status,
            "issues": issues
        })

    return report
