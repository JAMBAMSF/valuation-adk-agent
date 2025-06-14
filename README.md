# Valuation Intelligence ADK Agent

This project is a Google Agent Development Kit (ADK)-based synthetic assistant that simulates an enterprise-grade company valuation expert for M&A and minority investment use cases.

---

## Features
- Modular agent design with `valuation_tools.py`
- Responds to: "Value Snowflake" or "Value Datadog"
- Simulates: financial ingestion → valuation → RAI compliance
- Container-ready for Cloud Run / GKE
- Valuates companies using revenue × industry multiple logic
- Applies P/E ratio threshold to simulate RAI (Responsible AI) checks
- Returns structured JSON output with context for continued dialogue
- Fully stateless and offline—no API dependencies or live data

---

## How to Run Locally

```bash
git clone https://github.com/yourusername/valuation-adk-agent.git
cd valuation-adk-agent
docker build -t valuation-agent .
docker run -p 8080:8080 valuation-agent
```

---

## Sample Request

```bash
curl -X POST http://localhost:8080/agent \
     -H "Content-Type: application/json" \
     -d '{ "text": "What is the value of Snowflake?" }'
```

### Sample Response

```json
{
  "response": "SNOW Valuation Report:\nValuation estimate: $16.80B\nAttention: High P/E ratio may indicate RAI risk. Review recommended.",
  "context": {
    "last_company": "SNOW"
  }
}
```

---

## Screenshots
_(Insert Dialogflow/Terminal screenshots here before submission)_

---

## Structure

```
valuation-adk-agent/
├── agent.yaml
├── agent.py
├── main.py
├── valuation_tools.py
├── requirements.txt
├── Dockerfile
├── README.md
└── screenshots/
```

---
