FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libnss3 libatk1.0-0 libatk-bridge2.0-0 \
    libcups2 libxkbcommon0 libxcomposite1 libxdamage1 \
    libxrandr2 libgbm1 libgtk-3-0 libasound2 \
    wget unzip && \
    rm -rf /var/lib/apt/lists/*

# Work inside /app
WORKDIR /app

# COPY backend requirements FIRST (because context = ROOT)
COPY backend/requirements.txt requirements.txt

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright
RUN pip install playwright && playwright install --with-deps

# Copy the entire backend folder
COPY backend/ .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
