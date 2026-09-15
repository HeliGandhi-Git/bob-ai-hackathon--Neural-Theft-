# THREATWISE Architecture

## Overview

THREATWISE follows a simple threat-intelligence processing pipeline:

```text
Multi-Source Alerts
        ↓
Alert Ingestion
        ↓
Alert Correlation
        ↓
Threat Scoring
        ↓
Priority Classification
        ↓
MITRE ATT&CK Mapping
        ↓
BLUF Generation
        ↓
Commander Dashboard
