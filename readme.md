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
   - Trigger deployment on Render via API

2. **Render**:
   - Application retrieval and deployment from GitHub repository
   - Auto-deploy disabled (managed by GitHub Actions)

### Docker Hub Image

The Docker image is pushed to Docker Hub for:
- Horizontal scaling (multiple deployment instances)
- Multi-environment deployments (dev/staging/prod)
- Platform portability (Kubernetes, AWS ECS, etc.)
- Disaster recovery scenarios

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