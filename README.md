# NavGuard

NavGuard is an automated navigation validation and telemetry analysis system designed to evaluate the quality of navigation software updates before fleet release.

The system simulates real-world vehicle telemetry, computes route quality metrics, detects regressions between software versions, and blocks releases that degrade driver experience.

---

## Why NavGuard Exists

Modern navigation systems are updated frequently and deployed to millions of vehicles over-the-air.  
Before release, each update must be validated to ensure it does not introduce regressions such as:
- Worse ETA accuracy
- Inefficient routing
- Increased wrong turns

NavGuard provides a data-driven validation pipeline that compares a new navigation version against a previously deployed version using measurable performance metrics.

---

## Core Concepts

NavGuard simulates two navigation versions:
- **v1** – currently deployed version
- **v2** – candidate update

Each version generates telemetry-style route data, which NavGuard analyzes to determine whether the update should be approved or blocked.

---

## Metrics Evaluated

- **ETA Accuracy** – Absolute ETA error percentage  
- **Route Efficiency** – Distance comparison across versions  
- **Turn Accuracy** – Number of wrong turns per route  

Lower values indicate better performance.

---

## Regression Detection

NavGuard automatically flags regressions when:
- ETA accuracy worsens
- Turn accuracy degrades
- Route efficiency decreases

Any detected regression results in a **FAIL** status, blocking the release.

---

## Architecture

data/ # Simulated fleet telemetry
src/
├── metrics/ # Route quality metrics
├── validation/ # Regression detection logic
├── api/ # FastAPI service
tests/ # Unit tests
dashboards/ # Visual validation reports

---
