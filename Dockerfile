# /Dockerfile  (place at repo root)
FROM mcr.microsoft.com/playwright/python:1.45.0-focal

WORKDIR /app

# Copy and install backend requirements
COPY backend/requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code and set working dir
COPY backend/ ./backend
WORKDIR /app/backend

# Expose and run
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
