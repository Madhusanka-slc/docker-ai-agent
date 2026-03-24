
# Docker AI Agent

A **comprehensive Docker-based AI agent system** that combines containerization with LangChain, LangGraph, and FastAPI. This project demonstrates how to build, deploy, and orchestrate AI agents using Docker, with integrations for Postgres, email automation, and multi-agent systems.

---

## Tech Stack

* **Docker** – Containerization and deployment
* **FastAPI** – Backend API framework
* **LangChain** – AI agent framework
* **LangGraph** – Multi-agent orchestration
* **Postgres** – Database with Docker volumes
* **OpenAI** – LLM integration
* **Railway / DigitalOcean** – Cloud deployment platforms

---

## Features

* **Docker Fundamentals** – Custom Dockerfiles, Docker Compose, volume mounting, and watch mode
* **AI Agent System** – LangChain tools, LangGraph supervisor, and multi-agent coordination
* **Email Automation** – Send and read emails via Gmail integration
* **Database Integration** – Postgres with SQLModel and FastAPI
* **Model Runner** – Run open-source models with Docker Model Runner
* **Multi-Platform Deployment** – Deploy to Railway and DigitalOcean
* **Production-Ready** – Environment variables, secrets management, and production API testing

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/Madhusanka-slc/docker-ai-agent.git
cd docker-ai-agent
```

Set up environment variables:

```bash
cp .env.sample .env
# Edit .env with your API keys and credentials
```

Run with Docker Compose:

```bash
docker compose up
```

For development with watch mode:

```bash
docker compose watch
```

Run FastAPI directly (without Docker):

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Now the application will be available at `http://localhost:8000`.
