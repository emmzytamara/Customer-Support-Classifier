# 🎫 PulseDesk AI - Customer Support Ticket Classifier

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://www.docker.com/)

> **Production-grade ML system for automated customer support ticket classification using fine-tuned DistilBERT achieving 94% accuracy**

Led end-to-end development and deployment.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [API Usage](#-api-usage)
- [Model Performance](#-model-performance)
- [Deployment](#-deployment)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Development](#-development)
- [Monitoring & Observability](#-monitoring--observability)
- [Author](#-author)
- [License](#-license)

---

## 🎯 Overview

PulseDesk AI is an intelligent customer support ticket classification system that automatically categorizes incoming support requests into four key categories: **Account**, **Billing**, **Technical**, and **Other**. Built with production-grade infrastructure, this system demonstrates enterprise-level MLOps practices including automated CI/CD, containerization, and comprehensive monitoring.

### Business Impact

- **⚡ 94% Classification Accuracy** - Reliable automated ticket routing
- **🚀 <50ms Inference Time** - Real-time predictions for immediate routing
- **📊 Prometheus Integration** - Full observability for production monitoring
- **🔄 Automated Deployment** - Zero-downtime deployments via GitHub Actions
- **🐳 Docker-First Architecture** - Consistent environments from dev to production

---

## 🔥 Key Features

### Machine Learning
- **Fine-tuned DistilBERT** for efficient text classification
- **Multi-class classification** with confidence scores for all categories
- **CPU-optimized inference** for cost-effective deployment
- **MLflow experiment tracking** for model versioning and metrics

### Backend Infrastructure
- **FastAPI** framework with async request handling
- **RESTful API** with automatic OpenAPI documentation
- **CORS-enabled** for cross-origin frontend integration
- **Health check endpoints** for load balancer integration

### DevOps & Monitoring
- **GitHub Actions CI/CD** pipeline for automated deployments
- **Docker containerization** for consistent environments
- **Prometheus metrics** for real-time monitoring
- **AWS EC2 deployment** with automated rollback capability

### User Interface
- **Interactive web UI** for testing and demonstrations
- **Real-time classification** with visual confidence indicators
- **Responsive design** for desktop and mobile

---

## 🏗️ Architecture

```
┌─────────────────┐
│   GitHub Repo   │
│   (Push to main) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ GitHub Actions  │ ◄── Automated CI/CD Pipeline
│   Workflow      │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│         AWS EC2 Instance            │
│  ┌──────────────┐  ┌─────────────┐ │
│  │   Backend    │  │     UI      │ │
│  │   (Docker)   │  │  (Docker)   │ │
│  │   Port 8000  │  │  Port 80    │ │
│  └──────┬───────┘  └──────┬──────┘ │
│         │                 │         │
│         ▼                 ▼         │
│  ┌────────────────────────────┐    │
│  │   DistilBERT Model        │    │
│  │   + Prometheus Metrics     │    │
│  └────────────────────────────┘    │
└─────────────────────────────────────┘
```

### Data Flow
1. **Input**: Customer support message via API or UI
2. **Preprocessing**: Text tokenization using DistilBERT tokenizer
3. **Inference**: Fine-tuned model prediction with confidence scores
4. **Metrics**: Prometheus captures latency and prediction counts
5. **Output**: Category label with full probability distribution

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Docker (optional, for containerized deployment)
- 4GB RAM minimum (for model loading)

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/emmzytamara/Customer-Support-Classifier.git
cd Customer-Support-Classifier-
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download the model**
```bash
chmod +x download_model.sh
./download_model.sh
```

4. **Run the application**
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

5. **Access the application**
- API: http://localhost:8000
- Interactive Docs: http://localhost:8000/docs
- Metrics: http://localhost:8000/metrics

### Docker Deployment

```bash
docker build -t pulsedesk-api .
docker run -d -p 8000:8000 --name pulsedesk-api pulsedesk-api
```

---

## 📡 API Usage

### Health Check
```bash
curl http://localhost:8000/health
```

### Classify Support Ticket
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "My account is locked"}'
```

**Response:**
```json
{
  "label": "account",
  "confidence": 0.94,
  "all_probabilities": {
