import json
from pathlib import Path

import streamlit as st

from correlation import correlate_alerts
from scoring import calculate_threat_score
from mitre_mapping import map_to_mitre
from bluf_generator import generate_bluf


st.set_page_config(
    page_title="THREATWISE",
    page_icon="🛡️",
    layout="wide",
)


@st.cache_data
def load_alerts():
    data_path = Path(__file__).parent.parent / "data" / "sample_alerts.json"

    with open(data_path, "r", encoding="utf-8") as file:
        return json.load(file)


def build_incidents(alerts):
    incidents = correlate_alerts(alerts)

    for incident in incidents:
        score_data = calculate_threat_score(incident["alerts"])
        mitre_data = map_to_mitre(incident["alerts"])
        bluf_data = generate_bluf(
            incident,
            score_data,
            mitre_data,
        )

        incident["score"] = score_data["score"]
        incident["priority"] = score_data["priority"]
        incident["reasons"] = score_data["reasons"]
        incident["mitre"] = mitre_data
        incident["bluf"] = bluf_data

    return incidents


st.title("🛡️ THREATWISE")
st.subheader("Threat Intelligence Correlation & Alert Prioritisation Assistant")

st.write(
    "From fragmented multi-source alerts to prioritised, "
    "actionable threat intelligence."
)

alerts = load_alerts()
incidents = build_incidents(alerts)

critical = sum(i["priority"] == "CRITICAL" for i in incidents)
high = sum(i["priority"] == "HIGH" for i in incidents)
medium = sum(i["priority"] == "MEDIUM" for i in incidents)
low = sum(i["priority"] == "LOW" for i in incidents)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Alerts", len(alerts))
col2.metric("Incidents", len(incidents))
col3.metric("Critical", critical)
col4.metric("High", high)
col5.metric("Medium / Low", medium + low)

st.divider()

st.header("Prioritised Threat Incidents")

priority_order = {
    "CRITICAL": 1,
    "HIGH": 2,
    "MEDIUM": 3,
    "LOW": 4,
}

incidents = sorted(
    incidents,
    key=lambda x: (
        priority_order.get(x["priority"], 5),
        -x["score"],
    ),
)

for incident in incidents:
    priority = incident["priority"]

    with st.expander(
        f'{incident["incident_id"]} — {priority} — '
        f'Score {incident["score"]}/100'
    ):
        st.subheader("Commander BLUF")

        st.info(incident["bluf"]["bluf"])

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Affected Hosts**")
            st.write(
                ", ".join(incident["bluf"]["affected_hosts"])
                or "Unknown"
            )

            st.write("**Source IPs**")
            st.write(
                ", ".join(incident["bluf"]["source_ips"])
                or "Unknown"
            )

        with col2:
            st.write("**Alert Sources**")
            st.write(
                ", ".join(incident["bluf"]["sources"])
                or "Unknown"
            )

            st.write("**MITRE ATT&CK Techniques**")

            if incident["bluf"]["mitre_techniques"]:
                for technique in incident["bluf"]["mitre_techniques"]:
                    st.write(f"• {technique}")
            else:
                st.write("No technique mapped")

        st.write("**Why was this prioritised?**")

        for reason in incident["reasons"]:
            st.write(f"• {reason}")

        st.write("**Correlated Alerts**")

        for alert in incident["alerts"]:
            st.json(alert)


st.divider()

st.header("Alert Feed")

st.dataframe(
    alerts,
    use_container_width=True,
)

st.caption(
    "THREATWISE MVP — Designed for rapid threat triage, "
    "explainable prioritisation, MITRE ATT&CK mapping, "
    "and commander-focused BLUF reporting."
)
