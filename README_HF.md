---
title: PulseDesk AI - Customer Support Classifier
emoji: 🎫
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
license: mit
app_port: 8000
---

# 🎫 PulseDesk AI - Customer Support Ticket Classifier

Automatically classify customer support messages into categories using fine-tuned DistilBERT achieving **94% accuracy**.

## 🔥 Features

- **DistilBERT-based classification** - State-of-the-art transformer model
- **Real-time predictions** - Fast inference with confidence scores
- **4 Ticket Categories**: Account, Billing, Technical, Other
- **FastAPI backend** - Modern async API with automatic documentation
- **Production-ready** - Docker deployment with MLflow tracking

## 🚀 API Usage

### Health Check
```bash
curl https://dkumi12-pulsedesk-ai.hf.space/health
```

### Classify Support Ticket
```bash
curl -X POST "https://dkumi12-pulsedesk-ai.hf.space/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "My account is locked and I cannot login"}'
```

### Response Format
```json
{
  "label": "account",
  "confidence": 0.94,
  "all_probabilities": {
    "account": 0.94,
    "billing": 0.03,
    "technical": 0.02,
    "other": 0.01
  },
  "latency": 0.023
}
```

## 🎯 Model Details

- **Architecture**: DistilBERT (distilbert-base-uncased)
- **Task**: Multi-class text classification
- **Accuracy**: 94%
- **Categories**: 4 (Account, Billing, Technical, Other)
- **Training**: Fine-tuned on customer support ticket dataset
- **Inference**: CPU-optimized for fast real-time classification

## 📊 Use Cases

- **Customer Support Automation** - Route tickets to appropriate teams
- **Priority Classification** - Identify urgent vs routine requests
- **Analytics Dashboard** - Analyze support trends by category
- **Chatbot Integration** - Enhance AI assistants with context awareness

## 🛠️ Tech Stack

- **Model**: DistilBERT (Hugging Face Transformers)
- **Backend**: FastAPI
- **Monitoring**: Prometheus + MLflow
- **Container**: Docker
- **Deployment**: Hugging Face Spaces

## 🔗 Links

- **GitHub Repository**: [Customer-Support-Classifier](https://github.com/dkumi12/Customer-Support-Classifier-)
- **API Documentation**: `/docs` endpoint (FastAPI auto-generated)
- **Metrics Endpoint**: `/metrics` (Prometheus format)

## 👨🏾‍💻 Author

**David Osei Kumi**  
AI/ML Engineer | Cloud & DevOps Enthusiast  
- GitHub: [@dkumi12](https://github.com/dkumi12)
- LinkedIn: [David Osei Kumi](https://linkedin.com/in/your-linkedin)

## 📝 License

MIT License - See LICENSE file for details

---

Built with ❤️ using Hugging Face Spaces
