def generate_bluf(incident, score_data, mitre_data):
    """
    Generates a concise BLUF investigation summary
    from a correlated incident.
    """

    priority = score_data["priority"]
    score = score_data["score"]
    alerts = incident["alerts"]

    hosts = sorted(
        {
            alert.get("host")
            for alert in alerts
            if alert.get("host")
        }
    )

    source_ips = sorted(
        {
            alert.get("source_ip")
            for alert in alerts
            if alert.get("source_ip")
        }
    )

    sources = sorted(
        {
            alert.get("source")
            for alert in alerts
            if alert.get("source")
        }
    )

    techniques = [
        f'{item["technique_id"]} - {item["technique"]}'
        for item in mitre_data
    ]

    if priority == "CRITICAL":
        assessment = "Immediate investigation is recommended."
    elif priority == "HIGH":
        assessment = "Priority investigation is recommended."
    elif priority == "MEDIUM":
        assessment = "Further investigation is recommended."
    else:
        assessment = "Routine monitoring is recommended."

    bluf = (
        f"BLUF: {priority} threat detected with a risk score of {score}/100. "
        f"{len(alerts)} related alerts were correlated across "
        f"{len(sources)} source(s). {assessment}"
    )

    return {
        "bluf": bluf,
        "incident_id": incident["incident_id"],
        "priority": priority,
        "risk_score": score,
        "affected_hosts": hosts,
        "source_ips": source_ips,
        "sources": sources,
        "mitre_techniques": techniques,
        "investigation_reasons": score_data["reasons"],
    }
