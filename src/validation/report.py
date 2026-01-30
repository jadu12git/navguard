import pandas as pd
import matplotlib.pyplot as plt
from src.metrics.eta_accuracy import eta_error_percentage

def generate_eta_report(v1_path, v2_path, output_path):
    v1 = pd.read_csv(v1_path)
    v2 = pd.read_csv(v2_path)

    routes = v1["route_id"]
    eta_v1 = []
    eta_v2 = []

    for route_id in routes:
        r1 = v1[v1["route_id"] == route_id].iloc[0]
        r2 = v2[v2["route_id"] == route_id].iloc[0]

        eta_v1.append(eta_error_percentage(r1["eta_seconds"], r1["actual_time_seconds"]))
        eta_v2.append(eta_error_percentage(r2["eta_seconds"], r2["actual_time_seconds"]))

    plt.figure()
    plt.plot(routes, eta_v1, label="v1 ETA Error")
    plt.plot(routes, eta_v2, label="v2 ETA Error")
    plt.xlabel("Route ID")
    plt.ylabel("ETA Error %")
    plt.legend()
    plt.title("ETA Accuracy Comparison")
    plt.savefig(output_path)
