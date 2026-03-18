# 🚀 PulseDesk AI - Multi-Platform Deployment Guide

This guide covers deploying PulseDesk AI to various cloud platforms beyond AWS EC2.

## 📋 Prerequisites

Before deploying to any platform, ensure you have:
- ✅ Docker installed locally (for testing)
- ✅ Google Drive model file ID: `1t-X6C2vL94D-m4e2Thd2HDclcbaPLN47`
- ✅ GitHub account with this repo
- ✅ Account on your chosen platform

---

## 🏆 **Recommended Platforms (Ranked)**

### **1. Railway.app** ⭐ BEST FOR THIS PROJECT
**Why:** Free tier, automatic HTTPS, great for ML apps, simple deployment

**Pros:**
- ✅ $5 free credits/month (enough for development)
- ✅ Automatic HTTPS with custom domains
- ✅ Zero-config Docker deployments
- ✅ Built-in CI/CD from GitHub
- ✅ Environment variables management
- ✅ Great for ML workloads

**Pricing:** $5/month in credits (free tier), then pay-as-you-go

**Deploy Steps:**
```bash
# 1. Go to railway.app and sign in with GitHub
# 2. Click "New Project" → "Deploy from GitHub repo"
# 3. Select: Customer-Support-Classifier-
# 4. Railway auto-detects Dockerfile
# 5. Add environment variable:
#    GDRIVE_FILE_ID = 1t-X6C2vL94D-m4e2Thd2HDclcbaPLN47
# 6. Click Deploy
```

**Railway URL:** Your app will be at `https://your-app.railway.app`

---

### **2. Render.com** ⭐ GREAT FREE TIER
**Why:** True free tier, no credit card required, automatic SSL

**Pros:**
- ✅ Completely free tier (with limitations)
- ✅ No credit card needed to start
- ✅ Automatic SSL certificates
- ✅ Easy GitHub integration
- ✅ Good documentation

**Cons:**
- ⚠️ Free tier spins down after 15 min inactivity (cold starts)
- ⚠️ 750 hours/month limit on free tier

**Pricing:** Free tier available, then $7/month

**Deploy Steps:**
1. Go to [render.com](https://render.com)
2. Sign in with GitHub
3. Click "New +" → "Web Service"
4. Connect your repo: `Customer-Support-Classifier-`
5. Configure:
   - **Name:** pulsedesk-ai
   - **Environment:** Docker
   - **Region:** Oregon (US West) or closest to you
   - **Branch:** main
   - **Dockerfile Path:** ./Dockerfile
6. Add Environment Variable:
   ```
   GDRIVE_FILE_ID = 1t-X6C2vL94D-m4e2Thd2HDclcbaPLN47
   ```
7. Click "Create Web Service"

**Render URL:** `https://pulsedesk-ai.onrender.com`

---

### **3. Google Cloud Run** ⭐ BEST FOR SCALABILITY
**Why:** Serverless, scales to zero, generous free tier, Google's infrastructure

**Pros:**
- ✅ 2 million requests/month free
- ✅ Scales automatically (including to zero)
- ✅ Fast cold starts
- ✅ Global CDN
- ✅ Pay only for actual usage

**Cons:**
- ⚠️ Requires Google Cloud account (credit card for verification)
- ⚠️ More complex initial setup

**Pricing:** Free tier: 2M requests/month, then $0.40 per million requests

**Deploy Steps:**
```bash
# 1. Install Google Cloud CLI
# https://cloud.google.com/sdk/docs/install

# 2. Login
gcloud auth login

# 3. Set project
gcloud config set project YOUR_PROJECT_ID

# 4. Build and push container to Google Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/pulsedesk-api

# 5. Deploy to Cloud Run
gcloud run deploy pulsedesk-api \
  --image gcr.io/YOUR_PROJECT_ID/pulsedesk-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GDRIVE_FILE_ID=1t-X6C2vL94D-m4e2Thd2HDclcbaPLN47 \
  --memory 2Gi \
  --timeout 300
```

**Cloud Run URL:** `https://pulsedesk-api-xxxxx.run.app`

---

### **4. Fly.io** ⭐ DEVELOPER-FRIENDLY
**Why:** Great developer experience, global edge deployment

**Pros:**
- ✅ Free tier: 3 shared-cpu VMs, 3GB storage
- ✅ Deploy globally in seconds
- ✅ Excellent CLI tool
- ✅ Auto-scaling

**Cons:**
- ⚠️ Requires credit card for verification
- ⚠️ Free tier is limited

**Pricing:** Free tier available, then $0.0000022/sec per VM

**Deploy Steps:**
```bash
# 1. Install flyctl
# Windows: 
# powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"

# 2. Login
fly auth login

# 3. Launch app (from repo directory)
cd Customer-Support-Classifier-
fly launch

# 4. Set environment variable
fly secrets set GDRIVE_FILE_ID=1t-X6C2vL94D-m4e2Thd2HDclcbaPLN47

# 5. Deploy
fly deploy
```

**Fly.io URL:** `https://pulsedesk-ai.fly.dev`

---

### **5. Azure Container Instances**
**Why:** Microsoft's simple container hosting

**Pros:**
- ✅ Simple deployment
- ✅ Per-second billing
- ✅ Good Azure integration

**Cons:**
- ⚠️ Requires Azure account
- ⚠️ No free tier for containers
- ⚠️ More expensive than alternatives

**Pricing:** ~$0.0000125/second (~$32/month for 1 vCPU)

**Deploy Steps:**
```bash
# 1. Install Azure CLI
# https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

# 2. Login
az login

# 3. Create resource group
az group create --name pulsedesk-rg --location eastus

# 4. Create container instance
az container create \
  --resource-group pulsedesk-rg \
  --name pulsedesk-api \
  --image YOUR_DOCKER_IMAGE \
  --dns-name-label pulsedesk-api \
  --ports 8000 \
  --environment-variables GDRIVE_FILE_ID=1t-X6C2vL94D-m4e2Thd2HDclcbaPLN47
```

---

### **6. DigitalOcean App Platform**
**Why:** Simple, affordable, good for prototypes

**Pros:**
- ✅ $5/month basic plan
- ✅ Simple UI
- ✅ Integrated monitoring

**Cons:**
- ⚠️ No free tier
- ⚠️ Less features than competitors

**Pricing:** Starting at $5/month

**Deploy Steps:**
1. Go to [digitalocean.com/products/app-platform](https://www.digitalocean.com/products/app-platform)
2. Sign in and click "Create App"
3. Connect GitHub repo
4. Select Dockerfile deployment
5. Set environment variable: `GDRIVE_FILE_ID`
6. Deploy

---

## 🎯 **My Recommendation for You:**

Based on your needs (portfolio project + potential production use):

### **For Portfolio/Demo:** → **Railway** or **Render**
- Railway: Better performance, $5 free credits
- Render: True free tier (with cold starts)

### **For Job Applications:** → **Google Cloud Run**
- Shows you know GCP
- Demonstrates serverless architecture
- Professional-grade deployment
- Great for "scalable ML deployment" talking point

### **Quick Test:** → **Render.com**
- Zero cost to start
- No credit card required
- Live in 5 minutes

---

## 📊 **Quick Comparison Table**

| Platform | Free Tier | Cost/Month | Ease of Setup | Best For |
|----------|-----------|------------|---------------|----------|
| **Railway** | $5 credits | $5+ | ⭐⭐⭐⭐⭐ | Development |
| **Render** | Yes (limited) | $0-7 | ⭐⭐⭐⭐⭐ | Portfolio |
| **Google Cloud Run** | 2M req/mo | Pay-per-use | ⭐⭐⭐ | Production |
| **Fly.io** | 3 VMs free | $0+ | ⭐⭐⭐⭐ | Edge Deploy |
| **Azure ACI** | No | $32+ | ⭐⭐⭐ | Enterprise |
| **DigitalOcean** | No | $5+ | ⭐⭐⭐⭐ | Simple Hosting |

---

## 🔐 **Important: Don't Forget**

For ANY platform you choose, you need to:

1. **Add GitHub Secret:**
   - Go to your repo → Settings → Secrets
   - Add: `GDRIVE_FILE_ID` = `1t-X6C2vL94D-m4e2Thd2HDclcbaPLN47`

2. **Test Locally First:**
   ```bash
   docker build -t pulsedesk-api .
   docker run -p 8000:8000 pulsedesk-api
   # Visit: http://localhost:8000/health
   ```

3. **Update Your Resume/Portfolio:**
   - Add the live deployment URL
   - Mention the platform (especially if it's GCP/Azure)
   - Highlight "serverless" or "auto-scaling" if applicable

---

## 🎬 **Next Steps:**

1. **Choose your platform** (I recommend Railway or Render for quick start)
2. **Push your updated code:**
   ```bash
   git add .
   git commit -m "feat: add Google Drive model download for multi-platform deployment"
   git push origin main
   ```
3. **Deploy to chosen platform** (follow steps above)
4. **Update your README** with the new live URL
5. **Add deployment badge** to README (optional but looks professional)

---

Need help with a specific platform? Let me know! 🚀
