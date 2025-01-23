run-backend:
    cd backend && uvicorn main:app --host 0.0.0.0 --port 8000

run-frontend
    cd frontend && npm run serve
