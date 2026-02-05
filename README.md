# MedFlow: Autonomous Clinical Workflow Agent

MedFlow is an Agentic AI system designed to automate patient triage and clinical scheduling. Unlike a standard chatbot, MedFlow uses a **ReAct (Reasoning and Acting)** framework to interact with hospital databases and medical guidelines to make autonomous decisions with human oversight.

## 🚀 Key Agentic Features

* **Multi-Step Reasoning**: The agent performs a "Plan-Act-Observe" loop. It identifies patients via SQL, retrieves clinical protocols via RAG (Retrieval-Augmented Generation), and decides on the next clinical step.
* **Human-in-the-Loop (HITL)**: High-risk actions (like emergency bookings) are gated behind a mandatory human approval step, demonstrating AI safety and governance.
* **Production Guardrails**: Implements `max_iterations` and structured output parsing to prevent agentic loops and hallucinations.

## 🛠️ Tech Stack
- **Framework**: LangChain / LangGraph
- **LLM**: GPT-4o-Turbo
- **Vector DB**: ChromaDB (for RAG)
- **Primary DB**: SQLite (Structured patient data)
- **Language**: Python 3.10+

## 📂 Directory Structure
MedFlow-Agent/
├── data/               # Folder for medical PDFs

├── db/                 # Folder for SQLite database

├── src/
│   ├── database.py     # SQL Tool Logic
│   ├── rag.py          # RAG/Vector DB Logic
│   └── agent.py        # LangChain Agent & Tools

├── main.py             # Entry point

├── requirements.txt    # Dependencies

└── README.md           # Documentation

## 📂 Project Structure
- `src/database.py`: Manages SQL interactions.
- `src/rag.py`: Handles vector embeddings and medical document retrieval.
- `src/agent.py`: Defines the agent logic and tool-calling schema.

## 🤖 How It Works (Example Case)
**User Input:** *"I am Gana. I had surgery last week and I'm feeling very dizzy."*

1.  **Thought**: I need to verify 'Gana' in the database.
2.  **Action**: Calls `check_patient_history("Gana")`.
3.  **Observation**: Patient is "Post-Surgery Recovery."
4.  **Thought**: I should check if 'dizziness' is a risk for post-surgery patients.
5.  **Action**: Calls `medical_knowledge_search("dizziness")`.
6.  **Observation**: "Red Flag: Immediate clinical review required."
7.  **Thought**: This is urgent. I will request an emergency booking.
8.  **Action**: Calls `request_emergency_booking` (Triggers Human Approval).
