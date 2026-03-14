# ✈️ AI Travel Planner

An **AI-powered Travel Planner** that generates personalized day-trip itineraries based on a user's destination and interests using **LLMs and LangChain**.

This project demonstrates **AI application development with production practices** like Docker containerization and Kubernetes deployment.

---

## 🌍 Project Overview

AI Travel Planner allows users to input:

* A **city**
* Their **interests** (e.g., food, culture, adventure)

The system uses an **LLM via LangChain** to generate a **custom travel itinerary** in a clean bulleted format.

Example:

Input:

```
City: Paris
Interests: Food, History
```

Output:

```
• Visit the Louvre Museum  
• Walk through Montmartre  
• Enjoy authentic French cuisine in Le Marais  
• Explore Notre-Dame Cathedral  
• Evening cruise on the Seine River
```

---

# 🚀 Features

* 🧠 AI-generated travel itineraries
* 🌎 City-based travel planning
* 🎯 Interest-based customization
* ⚡ Fast API powered backend
* 🐳 Docker containerization
* ☸️ Kubernetes deployment ready
* 📦 Clean modular project structure

---

# 🛠️ Tech Stack

| Technology      | Usage                     |
| --------------- | ------------------------- |
| Python          | Core programming language |
| LangChain       | LLM orchestration         |
| OpenAI / LLM    | AI itinerary generation   |
| Docker          | Containerization          |
| Kubernetes      | Deployment                |
| FastAPI / Flask | API backend               |

---

# 📂 Project Structure

```
## 📂 Project Structure

```text
AI-TRAVEL-PLANNER
│
├── src/                         # Main application source code
│
│   ├── chains/                  # LLM prompt chains
│   │   ├── __init__.py
│   │   └── itinerary.py
│   │
│   ├── config/                  # Configuration settings
│   │   ├── __init__.py
│   │   └── config.py
│   │
│   ├── core/                    # Core application logic
│   │   ├── __init__.py
│   │   └── planner.py
│   │
│   ├── utils/                   # Utility modules
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   └── custom_exception.py
│   │
│   └── __init__.py
│
├── txt/                         # Text resources / prompts
│
├── venv/                        # Virtual environment (ignored in git)
│
├── .env                         # Environment variables
├── .gitignore                   # Git ignored files
├── app.py                       # Application entry point
├── Dockerfile                   # Docker container configuration
├── k8s-deployment.yaml          # Kubernetes deployment configuration
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup
└── README.md                    # Project documentation
```
### Key Components

- **chains/** → Contains LangChain prompt templates and AI logic  
- **config/** → Handles configuration settings for the application  
- **core/** → Main business logic of the travel planner  
- **utils/** → Logging and custom exception handling  
- **app.py** → Entry point of the application  
- **Dockerfile** → Containerizes the application  
- **k8s-deployment.yaml** → Kubernetes deployment configuration


# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Shubham37204/AI-TRAVEL-PLANNER.git
cd AI-TRAVEL-PLANNER
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

---

# 🐳 Run Using Docker

Build the Docker image

```bash
docker build -t ai-travel-planner .
```

Run the container

```bash
docker run -p 8000:8000 ai-travel-planner
```

---

# ☸️ Kubernetes Deployment

Apply the Kubernetes configuration

```bash
kubectl apply -f k8s-deployment.yaml
```

Check pods

```bash
kubectl get pods
```

Check services

```bash
kubectl get svc
```
