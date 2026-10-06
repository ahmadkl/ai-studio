# AI Studio

AI Studio is a starter platform for creative AI workflows, including:
- AI chat
- Text-to-image generation
- Image animation
- Text-to-video generation
- Video extension/interpolation
- Persona/profile persistence

## Tech stack
- Frontend: Next.js + TypeScript
- Backend: FastAPI
- Background jobs: Celery + Redis
- Containerization: Docker Compose

## Quick start

```bash
docker compose up --build
```

Then open:
- Frontend: http://localhost:3000
- API docs: http://localhost:8000/docs

## Structure

```text
backend/     FastAPI server
frontend/    Next.js frontend
workers/     Celery worker tasks
scripts/     Utility scripts
storage/     Generated files
```

## Notes
This is an MVP scaffold for later integration with real LLM, image, and video models.
