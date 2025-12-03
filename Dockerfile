# /Dockerfile  (place at repo root)
FROM mcr.microsoft.com/playwright/python:1.45.0-focal

# Working directory
WORKDIR /app

# Copy and install backend requirements (backend/requirements.txt)
COPY backend/requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ ./backend
WORKDIR /app/backend

# Expose port
EXPOSE 8000

# Default command to run the FastAPI web server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
