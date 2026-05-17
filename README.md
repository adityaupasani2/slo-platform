# SLO Platform with Error Budget Tracking

A production-grade SLO (Service Level Objective) platform built on Kubernetes, implementing Google SRE error budget methodology with real-time burn rate alerting.

## Architecture

FastAPI App → Prometheus → Sloth SLO Rules → Grafana Dashboard
↓
Alertmanager → Burn Rate Alerts

## Components

- **FastAPI** — Sample app exposing `/metrics` endpoint with simulated error rates
- **Prometheus** — Metrics collection and SLO recording rule evaluation
- **Sloth** — SLO-as-code framework generating multi-window burn rate rules
- **Alertmanager** — Multi-window burn rate alerting (fast burn + slow burn)
- **Grafana** — Error budget dashboard with real-time burn rate visualization

## SLOs Defined

| SLO | Target | Error Budget |
|-----|--------|--------------|
| Availability | 99.9% | 43 min/month |
| Latency p99 | 95% under 200ms | 36 min/month |

## Alerting Strategy

| Alert | Window | Burn Rate | Severity |
|-------|--------|-----------|----------|
| FastBurn | 5m + 1h | 14.4x | Critical |
| SlowBurn | 6h + 1d | 6x | Warning |

## Quick Start

```bash
# Start cluster
make cluster-start

# Deploy monitoring stack
make deploy-monitoring

# Deploy app
make deploy-app

# Port forward
make port-forward
```

## Key Results

- Implemented SLO-as-code using Sloth with 99.9% availability target
- Multi-window burn rate alerting detecting budget exhaustion 2hrs before breach
- Real-time error budget dashboard tracking 30-day rolling compliance
- Automated chaos simulation triggering burn rate alerts within 60 seconds

## Tech Stack

Kubernetes · Prometheus · Grafana · Alertmanager · Sloth · FastAPI · Python · Helm · GitHub Actions