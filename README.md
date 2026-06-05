# 🚀 StartupLens AI

StartupLens AI is an AI-powered startup validation platform that helps entrepreneurs, students, and innovators evaluate startup ideas before investing time and resources.

The platform leverages Generative AI to provide:

- 📈 Startup Validation
- 🏢 Competitor Analysis
- 📊 Market Research
- 🚀 Startup Blueprint Generation

---

## 🌟 Features

### 📈 Startup Validation
Analyze startup ideas and receive:

- Innovation Score
- Market Potential Score
- Competition Level
- Success Probability
- AI Recommendations

### 🏢 Competitor Analysis

Identify:

- Existing Competitors
- Market Gaps
- Opportunity Level

### 📊 Market Research

Generate:

- TAM (Total Addressable Market)
- SAM (Serviceable Addressable Market)
- SOM (Serviceable Obtainable Market)
- Market Growth Rate
- Target Audience Insights

### 🚀 Startup Blueprint Generator

Automatically generate:

- Executive Summary
- Problem Statement
- Solution
- Target Audience
- Revenue Model
- Go-To-Market Strategy
- Funding Recommendations

---

## 🏗️ Project Architecture

```text
User Idea
    │
    ▼
Frontend (Streamlit)
    │
    ▼
Backend (FastAPI)
    │
    ├── Idea Agent
    ├── Competitor Agent
    ├── Market Research Agent
    └── Blueprint Agent
    │
    ▼
Gemini AI
    │
    ▼
Structured Startup Insights
```

---

## 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- FastAPI
- Python

### AI

- Google Gemini API

### Utilities

- Requests
- Dotenv

---

## 📂 Project Structure

```text
StartupLensAI/
│
├── backend/
│   ├── agents/
│   │   ├── idea_agent.py
│   │   ├── competitor_agent.py
│   │   ├── market_agent.py
│   │   └── blueprint_agent.py
│   │
│   ├── services/
│   │   └── gemini_service.py
│   │
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── docs/
├── tests/
├── deployment/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/anupala21/StartupLensAI.git
cd StartupLensAI
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```
Activate:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env File

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### 5. Start Backend

```bash
uvicorn backend.main:app --reload
```

### 6. Start Frontend

```bash
streamlit run frontend/app.py
```

## 🔮 Future Enhancements

- Investor Pitch Deck Generation
- PDF Report Export
- User Authentication
- Startup Idea History
- Investor Matching System
- Cloud Deployment
- Startup Recommendation Engine

---

## 🎯 Use Cases

- Student Entrepreneurs
- Startup Founders
- Innovation Labs
- Incubators & Accelerators
- Business Analysts
- Product Managers

---

## 👩‍💻 Author

**Vaishnavi Anupala**

GitHub:
https://github.com/anupala21

LinkedIn:
https://www.linkedin.com/in/vaishnavi-anupala-8a0964369/

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
