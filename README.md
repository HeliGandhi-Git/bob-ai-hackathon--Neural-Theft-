# 🚀 THREATWISE

> ### AI-Powered Threat Intelligence Correlation & Alert Prioritisation Assistant
>
> **From thousands of fragmented alerts to prioritised, actionable threat intelligence.**

---

## 👥 Team

| Field         | Value                                                                        |
| ------------- | ---------------------------------------------------------------------------- |
| **Team Name** | Neural Theft                                                                 |
| **Track**     | AI                                                                           |
| **Team Lead** | Jash Mandani — [20pgce011@charusat.edu.in](mailto:26pgce011@charusat.edu.in) |
| **Members**   | Heli Gandhi, Tanisha Kapila, Vansh Desai                                     |

### Team Members 

| Name               | Role                              | Email                                                         |
| ------------------ | --------------------------------- | ------------------------------------------------------------- |
| **Jash Mandani**   | Team Lead / Project Coordination  | [20pgce011@charusat.edu.in](mailto:26pgce011@charusat.edu.in) |
| **Heli Gandhi**    | AI & Application Development      | [26pgce005@charusat.edu.in](mailto:26pgce005@charusat.edu.in) |
| **Tanisha Kapila** | Research, Testing & Documentation | [26pgce009@charusat.edu.in](mailto:26pgce009@charusat.edu.in) |
| **Vansh Desai**    | UI/UX, Presentation & Testing     | [26pgce004@charusat.edu.in](mailto:26pgce004@charusat.edu.in) |

---

## 🎯 Problem Statement

Defence analysts receive thousands of alerts every day from SIEM systems, cyber sensors, satellite feeds, and threat intelligence reports, often in different formats. Manually reviewing and correlating this volume of information is difficult and can result in genuine threats being missed or valuable resources being wasted investigating false positives.

Our project addresses this challenge by helping defence analysts identify related security events, prioritise genuine threats, map suspicious activities to the MITRE ATT&CK framework, and generate clear BLUF (Bottom Line Up Front) investigation summaries for faster decision-making.

---

## 💡 Solution

**THREATWISE** is an AI-powered threat intelligence correlation and alert prioritisation assistant designed to transform fragmented security alerts into actionable incidents.

The system ingests structured alerts from multiple simulated sources, normalises and correlates related events using shared indicators such as IP addresses, hosts, users, and timestamps, calculates a threat priority score, identifies likely false positives, maps suspicious behaviour to relevant MITRE ATT&CK techniques, and generates concise BLUF summaries with recommended investigation actions.

---

## ✨ Key Features

* **Multi-Source Threat Ingestion:** Processes structured threat alerts originating from simulated SIEM systems, cyber sensors, and threat intelligence feeds.
* **Alert Correlation:** Groups related alerts into incidents using common indicators such as source IP, destination IP, affected host, user, and event patterns.
* **Threat Prioritisation:** Calculates an explainable risk score and categorises incidents as **Critical, High, Medium, or Low** priority.
* **False Positive Identification:** Flags low-confidence and weakly correlated alerts as likely false positives to help analysts focus on significant threats.
* **MITRE ATT&CK Mapping:** Maps recognised suspicious behaviours to relevant MITRE ATT&CK techniques to provide structured investigation context.
* **AI-Powered BLUF Summaries:** Generates concise Bottom Line Up Front summaries containing the threat assessment, confidence, evidence, affected assets, and recommended actions.
* **Commander-Focused Dashboard:** Presents prioritised incidents and investigation details in a clear, easy-to-understand format.

---

## 🔄 How THREATWISE Works

```text
Multiple Threat Sources
(SIEM / Sensors / Intelligence Reports)
                │
                ▼
        Threat Data Ingestion
                │
                ▼
        Data Normalisation
                │
                ▼
        Alert Correlation Engine
                │
                ▼
      ┌─────────┴─────────┐
      ▼                   ▼
Likely False Positive   Correlated Incident
      │                   │
      └─────────┬─────────┘
                ▼
        Threat Risk Scoring
                │
                ▼
       Priority Classification
   Critical / High / Medium / Low
                │
                ▼
      MITRE ATT&CK Mapping
                │
                ▼
       AI-Powered BLUF Summary
                │
                ▼
     Actionable Commander View
```

---

## 🧠 Example Incident Analysis

### Incoming Alerts

**SIEM Alert**

* Multiple failed authentication attempts
* Source IP identified as suspicious
* Target: `FINANCE-PC-07`

**Endpoint Sensor Alert**

* Suspicious PowerShell execution detected
* Host: `FINANCE-PC-07`

**Threat Intelligence Feed**

* Source IP associated with malicious activity
* High threat intelligence confidence

### THREATWISE Correlation

The system identifies the common affected host and related suspicious indicators, correlating the separate alerts into a single investigation incident.

### Example Output

**Priority:** 🔴 CRITICAL

**Confidence:** High

**MITRE ATT&CK:** `T1059.001 — PowerShell`

**BLUF:**

> A high-confidence malicious activity cluster has been identified affecting FINANCE-PC-07. Multiple failed authentication attempts were correlated with suspicious PowerShell execution and a threat intelligence indicator associated with malicious activity. Immediate investigation and containment are recommended.

**Recommended Actions:**

1. Isolate the affected endpoint.
2. Block the identified malicious indicator.
3. Investigate associated authentication activity.
4. Review PowerShell execution history.
5. Validate whether additional systems are affected.

---

## 🛠️ Tech Stack

| Category                | Technologies                                             |
| ----------------------- | -------------------------------------------------------- |
| **Languages**           | Python, JavaScript, HTML, CSS                            |
| **Frameworks**          | Streamlit                                                |
| **AI Technologies**     | IBM Bob, AI-assisted threat analysis and BLUF generation |
| **Threat Intelligence** | MITRE ATT&CK framework                                   |
| **Data Processing**     | Python, JSON, Pandas                                     |
| **Databases**           | Structured JSON-based prototype data                     |
| **Other**               | GitHub, GitHub Actions                                   |

> **Note:** The final IBM technology entry will be updated to accurately reflect the IBM BoB components and services used during development.

---

## 📁 Repository Structure

```text
├── .github/                         # GitHub Actions and repository workflows
│
├── src/                             # Application source code
│   ├── app.py                       # Main THREATWISE application
│   ├── correlation.py               # Alert correlation logic
│   ├── scoring.py                   # Threat scoring and prioritisation
│   ├── mitre_mapping.py             # MITRE ATT&CK mapping logic
│   └── bluf_generator.py            # BLUF summary generation
│
├── data/                            # Sample multi-source threat feeds
│   └── sample_alerts.json           # Sample SIEM, sensor and intelligence alerts
│
├── docs/                            # Written documentation
│   ├── problem-statement.md
│   ├── solution-overview.md
│   ├── architecture.md
│   └── setup-guide.md
│
├── demo/                            # Demo artifacts
│   ├── screenshots/                 # Application screenshots
│   ├── demo-video-link.txt          # Demo video link
│   └── live-demo-url.txt            # Live demo link, if available
│
├── presentation/                    # Project presentation
│   └── slides.pdf
│
├── requirements.txt                 # Python dependencies
├── README.md                        # Project overview
└── submission.yaml                  # Structured hackathon submission metadata
```

---

## ⚡ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/HeliGandhi-Git/bob-ai-hackathon-neuraltheft.git
cd bob-ai-hackathon-neuraltheft
```

### 2. Create and activate a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run THREATWISE

```bash
streamlit run src/app.py
```

### 5. Open the application

After starting Streamlit, open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

---

## 🖥️ Demo

| Artifact        | Link                                                     |
| --------------- | -------------------------------------------------------- |
| 📹 Demo Video   | [See demo/demo-video-link.txt](demo/demo-video-link.txt) |
| 🌐 Live Demo    | [See demo/live-demo-url.txt](demo/live-demo-url.txt)     |
| 🖼️ Screenshots | [See demo/screenshots/](demo/screenshots/)               |
| 📊 Presentation | [See presentation/](presentation/)                       |

---

## 🎯 Expected Impact

THREATWISE is designed to help security and defence analysts:

* Reduce alert fatigue.
* Reduce time spent manually reviewing unrelated alerts.
* Prioritise potentially genuine threats.
* Identify relationships between events from multiple sources.
* Provide structured MITRE ATT&CK context.
* Produce concise and actionable threat summaries.
* Support faster commander and analyst decision-making.

---

## ⚠️ Known Limitations

> We prioritise transparency about the current prototype.

* **Prototype Data Sources:** The current MVP uses structured sample threat feeds rather than direct connections to production SIEM, satellite, or enterprise cyber sensor systems.
* **Rule-Based Correlation:** The initial correlation engine uses explainable rules and shared indicators; future versions can incorporate advanced machine-learning models and graph-based correlation.
* **Limited MITRE Coverage:** The prototype maps a selected set of common suspicious behaviours to MITRE ATT&CK techniques and does not yet cover the complete framework.
* **No Production Authentication:** User authentication and enterprise role-based access control are outside the scope of the current hackathon MVP.
* **Human Analyst Review:** THREATWISE is designed to assist analysts and commanders, not replace human investigation and decision-making.

---

## 🔮 Future Scope

Future versions of THREATWISE could include:

* Integration with live SIEM and security telemetry platforms.
* Real-time threat feed ingestion.
* Advanced machine-learning-based anomaly detection.
* Graph-based threat and entity correlation.
* Expanded MITRE ATT&CK coverage.
* Integration with additional threat intelligence platforms.
* Historical incident analysis and trend detection.
* Automated response recommendations and SOAR integration.
* Role-based dashboards for analysts and commanders.
* Continuous AI-assisted threat assessment using IBM technologies.

---

## 🏅 What We're Most Proud Of

The strongest aspect of **THREATWISE** is its ability to bring together multiple stages of threat analysis into one clear workflow: **ingestion, correlation, prioritisation, MITRE ATT&CK mapping, and commander-focused BLUF reporting**.

Instead of simply displaying another list of alerts, our solution focuses on the actual problem analysts face: turning a large volume of fragmented security information into a small number of understandable, prioritised, and actionable incidents. The project combines explainable threat scoring with structured cybersecurity knowledge and AI-assisted summarisation to support faster and more informed decision-making.

---

## 🛡️ THREATWISE

### From Alert Overload to Actionable Intelligence.

**Team Neural Theft**
IBM BoB AI Innovation Hackathon 2026
