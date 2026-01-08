# Backend Mon Assiette

FastAPI backend for calorie tracking

## 🔗 Deployment

Deployed application: https://backend-assiette.onrender.com

## 🚀 CI/CD Pipeline

Commit on `main` → GitHub Actions → Render

### Current Architecture

1. **GitHub Actions**:
   - Docker image build
   - Push to Docker Hub (`natalie2201/fastapi-test`)
   - Trigger deployment on Render

2. **Render**:
   - Application retrieval and deployment
   - Auto-deploy disabled (managed by GitHub Actions)

### Required Secrets

GitHub Secrets configuration:
- `DOCKER_USERNAME`: Docker Hub username
- `DOCKER_PASSWORD`: Docker Hub token
- `DOCKER_NAMESPACE`: Docker Hub namespace
- `MY_RENDER_SERVICE_ID`: Render service ID
- `MY_RENDER_API_KEY`: Render API key

## 📚 Technologies

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Hosting**: Render

---

**Note**: Exercise 3.2 from "DevOps with Docker" MOOC (University of Helsinki)

### Evolution

**Option 1 (initial)**: Render directly monitors changes on `main`
**Option 2 (current)**: GitHub Actions triggers deployment on Render via API

The Docker image is also available on Docker Hub for future use.