def calculate_threat_score(alerts):
    """
    Calculates an explainable threat score from correlated alerts.
    Score range is capped at 100.
    """

    score = 0
    reasons = []

    for alert in alerts:
        event = alert.get("event", "").lower()
        severity = alert.get("severity", "").lower()
        confidence = alert.get("ti_confidence", 0)

        if severity == "critical":
            score += 30
            reasons.append("Critical-severity alert detected")

        elif severity == "high":
            score += 20
            reasons.append("High-severity alert detected")

        if "malicious" in event:
            score += 30
            reasons.append("Known malicious indicator detected")

        if "powershell" in event:
            score += 20
            reasons.append("Suspicious PowerShell activity detected")

        if confidence >= 0.90:
            score += 10
            reasons.append("High threat-intelligence confidence")

    # Multiple alerts from different sources increase confidence
    sources = {alert.get("source") for alert in alerts}

    if len(alerts) >= 2:
        score += 10
        reasons.append("Multiple related alerts correlated")

    if len(sources) >= 2:
        score += 10
        reasons.append("Evidence confirmed by multiple sources")

    score = min(score, 100)

    if score >= 80:
        priority = "CRITICAL"
    elif score >= 60:
        priority = "HIGH"
    elif score >= 30:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    # Remove duplicate reasons while preserving order
    reasons = list(dict.fromkeys(reasons))

    return {
        "score": score,
        "priority": priority,
        "reasons": reasons,
    }
