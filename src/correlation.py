from collections import defaultdict


def correlate_alerts(alerts):
    """
    Groups related security alerts into incidents.

    Alerts are correlated using the affected host. This allows
    multiple signals from different sources to be treated as
    one investigation.
    """

    groups = defaultdict(list)

    for alert in alerts:
        key = (
            alert.get("host")
            or alert.get("indicator")
            or alert.get("source_ip")
            or "unknown"
        )

        groups[key].append(alert)

    incidents = []

    for index, (key, grouped_alerts) in enumerate(groups.items(), start=1):
        incidents.append(
            {
                "incident_id": f"INC-{index:03d}",
                "correlation_key": key,
                "alerts": grouped_alerts,
            }
        )

    return incidents
