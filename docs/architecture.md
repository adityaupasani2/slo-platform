# Architecture

## Components
- **FastAPI App** — exposes /metrics endpoint
- **Prometheus** — scrapes metrics, evaluates SLO recording rules
- **Sloth** — generates SLO recording rules from YAML specs
- **Alertmanager** — fires burn rate alerts
- **Grafana** — error budget dashboards

## Flow
FastAPI → Prometheus → Sloth Rules → Grafana Dashboard
                     ↓
                Alertmanager → Alerts