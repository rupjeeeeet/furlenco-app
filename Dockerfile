# Use Playwright image matching your requirements.txt version (1.45.0)
FROM mcr.microsoft.com/playwright/python:v1.45.0-jammy

WORKDIR /app

# Copy and install backend requirements
COPY backend/requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers (Chromium is usually sufficient)
RUN playwright install chromium

# Copy backend code
COPY backend/ ./backend

# Set working directory to backend
WORKDIR /app/backend

# Expose port
EXPOSE 8000

# Run the application (Railway will inject $PORT)
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}