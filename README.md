# Furlenco App

## Project Title & Description

This project is a web application designed to scrape data from Furlenco, store it in a PostgreSQL database, and leverage a Retrieval-Augmented Generation (RAG) chatbot for product information retrieval. It combines web scraping, database management, and natural language processing to provide users with an interactive experience.

## Key Features & Benefits

*   **Web Scraping:** Automatically scrapes product data from Furlenco using Playwright.
*   **Database Storage:** Stores scraped data in a PostgreSQL database for efficient querying and management.
*   **RAG Chatbot:** Integrates a RAG chatbot powered by Langchain (implied), allowing users to ask questions about Furlenco products and receive contextually relevant answers.
*   **Dockerized:** Easily deployable using Docker for consistent environments across different platforms.
*   **API:** Provides a FastAPI-based API for accessing product data and interacting with the chatbot.

## Prerequisites & Dependencies

Before you begin, ensure you have the following installed:

*   **Docker:** [https://www.docker.com/](https://www.docker.com/)
*   **Node.js:** [https://nodejs.org/](https://nodejs.org/) (Required by Playwright)
*   **Python 3.8+:** [https://www.python.org/](https://www.python.org/)
*   **pip:** Python package installer (usually included with Python)

And the following dependencies:

*   **Python Dependencies:** Specified in `backend/requirements.txt` (install using `pip install -r backend/requirements.txt`).  Key dependencies include:
    *   FastAPI
    *   SQLAlchemy
    *   psycopg2 (PostgreSQL driver)
    *   Uvicorn
    *   python-dotenv
    *   Playwright

## Installation & Setup Instructions

Follow these steps to install and set up the project:

1.  **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd furlenco-app
    ```

2.  **Set up Environment Variables:**

    Create a `.env` file in the `backend/` directory and add the following environment variables:

    ```
    DATABASE_URL=<your_postgresql_connection_string>
    ```

    Replace `<your_postgresql_connection_string>` with your actual PostgreSQL connection string.  Example:

    ```
    DATABASE_URL=postgresql://user:password@host:port/database
    ```

3.  **Build and Run the Docker Container:**

    ```bash
    docker build -t furlenco-app .
    docker run -p 8000:8000 furlenco-app
    ```

    This will build a Docker image named `furlenco-app` and run it, exposing the API on port 8000.

4.  **(Optional) Initialize the Database:**

    The `init_db.py` script creates the necessary database tables.  This is typically done automatically on first run by `main.py`, but if you have issues you can run it manually from inside the container by first getting a shell:

    ```bash
    docker exec -it <container_id> bash
    ```

    Find the container id via `docker ps`.  Then:

    ```bash
    cd backend
    python init_db.py
    ```

5.  **(Optional) Generate Embeddings:**

    The `generate_embeddings.py` script generates embeddings for product chunks and saves them to a vector store. Run inside container (see step 4):

    ```bash
    cd backend
    python generate_embeddings.py
    ```

## Usage Examples & API Documentation

The API exposes several endpoints:

*   **`/` (GET):**  Health Check.

*   **`/scrape` (POST):** Initiates the scraping process.  This endpoint is responsible for collecting product data from Furlenco.

*   **`/products` (GET):** Retrieves a list of products from the database.

*   **`/chat` (POST):**  Interacts with the RAG chatbot.  Send a POST request with a JSON payload containing a "question" field.  Example:

    ```json
    {
        "question": "What is the price of a sofa?"
    }
    ```

    The API will return the chatbot's response.

*  **`/init_db` (POST):** Initializes the database. Creates tables (only for manual setup or debug).

You can access the API documentation at `http://localhost:8000/docs` after running the application.  This is provided by FastAPI and allows you to explore the API endpoints and test them directly in your browser.

## Configuration Options

*   **`DATABASE_URL`:**  The PostgreSQL connection string, as described in the Installation section.  This must be set as an environment variable.

*   **`PORT`:** The port the application listens on.  Defaults to 8000 if not specified as an environment variable.

## Contributing Guidelines

Contributions are welcome! To contribute to this project, please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, concise messages.
4.  Submit a pull request to the main branch.

Please ensure your code adheres to the project's coding style and includes relevant tests.

## License Information

License not specified. All rights reserved.

## Acknowledgments

*   This project leverages the following open-source libraries and tools:
    *   FastAPI
    *   SQLAlchemy
    *   Playwright
    *   Uvicorn
    *   python-dotenv
