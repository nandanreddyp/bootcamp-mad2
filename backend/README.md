# Bootcamp-MAD2

## How to Run the Project

### Backend (Flask)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend (Vite)

```bash
cd frontend
npm install
npm run dev
```

### ⚙️ Celery (Asynchronous Tasks)

> Make sure **Redis** is running on `localhost:6379` and mailhog is running on `localhost:8025`.

#### Start Celery Worker

```bash
cd backend
# Linux/macOS
celery -A celery_app.celery worker --loglevel=info

# Windows (must use solo pool)
celery -A celery_app.celery worker --loglevel=info --pool=solo
```

#### Start Celery Beat Scheduler

```bash
cd backend
celery -A celery_app.celery beat --loglevel=info
```

