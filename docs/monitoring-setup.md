# Monitoring Stack Setup

## Prerequisites
- minikube running
- helm installed

## Deploy
```bash
make deploy-monitoring
```

## Access
- Grafana: `kubectl port-forward svc/kube-prometheus-stack-grafana 3000:80 -n monitoring`
- Prometheus: `kubectl port-forward svc/kube-prometheus-stack-prometheus 9090:9090 -n monitoring`

## Credentials
- Grafana: admin/admin
