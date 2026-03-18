import time
import torch
import mlflow
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from prometheus_client import Counter, Histogram, generate_latest
import os

app = FastAPI(title="Group D Support Ticket Classifier API")

# -----------------------------
# SERVE STATIC FILES (UI)
# -----------------------------
if os.path.exists("/app/static"):
    app.mount("/static", StaticFiles(directory="/app/static"), name="static")

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# PROMETHEUS METRICS
# -----------------------------
REQUEST_COUNT = Counter(
    "api_request_count", "Number of requests made to the API", ["endpoint"]
)

PREDICTION_TIME = Histogram(
    "prediction_processing_seconds", "Time spent processing predictions"
)

# -----------------------------
# MLflow CONFIG
# -----------------------------
mlflow.set_tracking_uri("file:/app/mlruns")   # <<< FIXED ABSOLUTE PATH
mlflow.set_experiment("group_d_customer_support_classifier")

# -----------------------------
# MODEL LOADING (FIXED PATH)
# -----------------------------
MODEL_PATH = "/app/model"     # <<< DO NOT TOUCH, WORKS WITH YOUR DOCKER COPY

print("🔥 Loading model from:", MODEL_PATH)

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

label_map = ["account", "billing", "other", "technical"]

# -----------------------------
# REQUEST SCHEMA
# -----------------------------
class RequestText(BaseModel):
    text: str

# -----------------------------
# ROOT - SERVE UI
# -----------------------------
@app.get("/", response_class=HTMLResponse)
def serve_ui():
    REQUEST_COUNT.labels(endpoint="/").inc()
    with open("/app/static/index.html", "r") as f:
        return f.read()

# -----------------------------
# HEALTH
# -----------------------------
@app.get("/health")
def health():
    REQUEST_COUNT.labels(endpoint="/health").inc()
    return {"status": "running"}

# -----------------------------
# METRICS
# -----------------------------
@app.get("/metrics")
def metrics():
    REQUEST_COUNT.labels(endpoint="/metrics").inc()
    return PlainTextResponse(generate_latest(), media_type="text/plain")

# -----------------------------
# PREDICTION
# -----------------------------
@app.post("/predict")
@PREDICTION_TIME.time()
def predict(payload: RequestText, request: Request):
    REQUEST_COUNT.labels(endpoint="/predict").inc()

    text = payload.text
    start = time.time()

    inputs = tokenizer(text, return_tensors="pt", truncation=True)

    with torch.no_grad():
        logits = model(**inputs).logits
        probs = torch.softmax(logits, dim=1)[0]

    top_idx = torch.argmax(probs).item()
    label = label_map[top_idx]
    confidence = float(probs[top_idx])
    all_probs = {label_map[i]: float(probs[i]) for i in range(len(label_map))}

    with mlflow.start_run(nested=True):
        mlflow.log_param("input_length", len(text))
        mlflow.log_param("predicted_label", label)
        mlflow.log_metric("confidence", confidence)
        mlflow.log_dict(all_probs, "probabilities.json")

    return {
        "label": label,
        "confidence": confidence,
        "all_probabilities": all_probs,
        "latency": time.time() - start,
    }
