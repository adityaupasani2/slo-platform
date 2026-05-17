# SLO Runbook

## Alert: SloAvailabilityFastBurn

**Severity:** Critical
**Meaning:** Error budget burning 14.4x faster than allowed. At this rate the monthly budget will be exhausted in ~2 hours.

### Steps
1. Check error rate: `sum(rate(app_requests_total{job="slo-demo-app",status=~"5.."}[5m]))`
2. Identify failing endpoint: `sum(rate(app_requests_total{job="slo-demo-app",status=~"5.."}[5m])) by (endpoint)`
3. Check pod logs: `kubectl logs -l app=slo-demo-app --tail=50`
4. Check pod status: `kubectl get pods | grep slo-demo-app`
5. Rollback if recent deploy: `kubectl rollout undo deployment/slo-demo-app`

---

## Alert: SloAvailabilitySlowBurn

**Severity:** Warning
**Meaning:** Error budget burning 6x faster than allowed. Budget will exhaust before month end if not addressed.

### Steps
1. Check error trends over 6h window
2. Identify if gradual degradation or spike
3. Create ticket for investigation
4. Monitor burn rate — if it increases to 14.4x, escalate to critical