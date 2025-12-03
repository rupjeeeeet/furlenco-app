FROM mcr.microsoft.com/playwright/python:v1.57.0-jammy

WORKDIR /app

# Copy and install backend requirements
# Ensure that backend/requirements.txt exists relative to the Dockerfile
COPY backend/requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code and set working dir
# Ensure that backend/ directory exists and contains your main.py
COPY backend/ ./backend
WORKDIR /app/backend

# Expose and run the application using uvicorn
EXPOSE 8000
# Assuming 'main' module contains a FastAPI/Starlette app named 'app'
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]