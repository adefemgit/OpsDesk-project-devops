Project name: OpsDesk
OpsDesk is an application for creating and tracking IT change requests. Users can create requests, view them, and update their status. This project focuses on deploying and operating the application reliably using Linux, Docker, CI/CD, monitoring, and backups.

Run from the project folder with your virtual environment active.

Install dependencies:
```bash
python -m pip install -r requirements.txt
```

Start the application:
```bash
python -m flask --app app run --port 8000
```

Run tests:
```bash
python -m pytest
```

Health endpoint: http://127.0.0.1:8000/health/live
Expected response: `{"status":"ok"}` with HTTP 200.


Added docker build and all dependencies neeed, run and health-check commands 

BUild:
-- docker build -t opsdesk:local 

Run:
docker run --rm --name opsdesk -p 127.0.0.1:8000:8000 opsdesk:local 

check from another terminal:
curl -i http://127.0.0.1:8000/health/live

Expected: HTTP 200 and {"status":"ok"}

Starting the stack: docker compose up -d --build
The difference between /health/live and /health/ready
Creating .env from .env.example and setting a local password

--Run with PostgreSQL

Copy `.env.example` to `.env` and set a local database password.
Keep `.env` out of Git.

-- Start the application and database:
```bash
docker compose up -d --build
```

--Health endpoints:
- `/health/live`: returns 200 when Flask responds.
- `/health/ready`: returns 200 when the database query succeeds, otherwise 503.

PostgreSQL data is stored in a named Docker volume.
