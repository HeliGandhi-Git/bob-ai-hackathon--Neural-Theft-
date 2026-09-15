MITRE_MAPPINGS = {
    "powershell": {
        "technique_id": "T1059.001",
        "technique": "PowerShell",
        "tactic": "Execution",
    },
    "failed login": {
        "technique_id": "T1110",
        "technique": "Brute Force",
        "tactic": "Credential Access",
    },
    "malicious ip": {
        "technique_id": "T1071",
        "technique": "Application Layer Protocol",
        "tactic": "Command and Control",
    },
}


def map_to_mitre(alerts):
    """
    Maps alert activity to selected MITRE ATT&CK techniques.
    """

    mappings = []

    for alert in alerts:
        event = alert.get("event", "").lower()

        for keyword, mapping in MITRE_MAPPINGS.items():
            if keyword in event:
                result = mapping.copy()
                result["alert_id"] = alert.get("alert_id")
                mappings.append(result)

    # Remove duplicate technique mappings
    unique = {}

    for mapping in mappings:
        unique[mapping["technique_id"]] = mapping

    return list(unique.values())
