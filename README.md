# Fetch Random Cat Images

A project featuring a FastAPI backend with UUID and cat image APIs, paired with a Streamlit frontend for interactive testing.

## Overview

This project includes:
- **Backend**: A FastAPI server providing UUID generation and random cat image fetching, located in `app/`.
- **Frontend**: A Streamlit interface to interact with the backend APIs, displaying responses, execution times, and cat images, located in `frontend/`.

## Project Structure

```
vaibhav-tiwari-manufac-fast-api/
├── .env                      # Environment variables for backend
├── .env.example              # Example environment variables for backend
├── .gitignore                # Git ignore rules
├── manufac_analytics_task_apis.json  # API collection (Postman / Thunder Client)
├── docker-compose.yml        # Docker Compose configuration
├── Dockerfile.backend        # Dockerfile for backend
├── Dockerfile.frontend       # Dockerfile for frontend
├── poetry.lock               # Python dependencies lock file
├── pyproject.toml            # Poetry project configuration
├── README.md                 # Project documentation 
│
├── app/                      # Backend source code (FastAPI)
│   ├── main.py               # FastAPI application entry point
│   ├── __init__.py           # Python package initializer
│   │
│   ├── api/                  # API route definitions
│   │   └── v1/
│   │       └── routes.py     # API route mappings (v1)
│   │
│   ├── config/               # Configuration management
│   │   └── settings.py       # App settings & environment variables
│   │
│   ├── middleware/           # Custom middlewares
│   │   ├── cors.py           # CORS middleware
│   │   ├── error_handler.py  # Exception & error handling
│   │   ├── gzip.py           # GZip compression middleware
│   │   ├── logger.py         # Request/response logging middleware
│   │   ├── rate_limit.py     # Rate limiting middleware
│   │   └── timeout.py        # Request timeout middleware
│   │
│   ├── schemas/              # Response & request models
│   │   └── response.py       # Standardized response schema
│   │
│   └── services/             # Business logic / Services layer
│       └── v1/
│           └── cat_service.py  # Cat API service logic
│
├── frontend/                 # Frontend source code (Streamlit)
│   ├── .env                  # Environment variables for frontend
│   ├── .env.example          # Example environment variables for frontend
│   ├── app.py                # Streamlit application entry point
│   ├── requirements.txt      # Frontend requirements
│   │
│   ├── components/           # Reusable frontend components
│   │   └── api_caller.py     # Utility to call backend APIs
│   │
│   └── config/               # Frontend configuration management
│       └── settings.py       # Frontend settings & environment variables

```

## Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Insomnia](https://insomnia.rest/) (optional, for API testing)
- Python 3.10+ (for local development)

## Setup and Running

### Using Docker Compose

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Vaibhav-crux/vaibhav-tiwari-manufac-fast-api.git
   cd vaibhav-tiwari-manufac-fast-api
   ```

2. **Configure Environment Variables**:
   - Copy `.env.example` to `/.env` and `frontend/.env` if not already present:
     ```bash
     cp .env.example app/.env
     cp frontend/.env.example frontend/.env
     ```
   - Edit `/.env`:
     ```
     CAT_API_URL=https://cataas.com/cat
     PORT=8000
     ```
   - Edit `frontend/.env`:
     ```
     API_BASE_URL=http://localhost:8000/v1
     PORT=8501
     ```

3. **Build and Run**:
   ```bash
   docker-compose up --build
   ```
   - Access:
     - **FastAPI Backend**: `http://localhost:8000`
     - **Streamlit Frontend**: `http://localhost:8501`

4. **Stop the Services**:
   ```bash
   docker-compose down
   ```

### Local Development

#### Backend
1. Navigate to the root directory:
   ```bash
   cd vaibhav-tiwari-manufac-fast-api
   ```
2. Install dependencies with Poetry:
   ```bash
   poetry install
   ```
3. Run the FastAPI server:
   ```bash
   poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

#### Frontend
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or source venv/bin/activate (Linux/Mac)
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## API Endpoints

The FastAPI backend provides the following endpoints, accessible at `http://localhost:8000/v1/` when running locally or via Docker.

### 1. GET /v1/uuid
- **Description**: Generates a random UUID v4.
- **URL**: `http://localhost:8000/v1/uuid`
- **Example Response**:
  ```json
  {
    "uuid": "550e8400-e29b-41d4-a716-446655440000"
  }
  ```

### 2. GET /v1/async-uuid
- **Description**: Generates a UUID v4 with a 3-second non-blocking delay.
- **URL**: `http://localhost:8000/v1/async-uuid`
- **Example Response**:
  ```json
  {
    "uuid": "123e4567-e89b-12d3-a456-426614174000"
  }
  ```

### 3. GET /v1/cat
- **Description**: Fetches a random cat image URL from an external API (configured via `CAT_API_URL`).
- **URL**: `http://localhost:8000/v1/cat`
- **Example Response**:
  ```json
  {
    "cat_image_url": "https://cataas.com/cat/abc123"
  }
  ```

## Testing with Insomnia

An Insomnia export file (`manufac_analytics_task_apis.json`) is included in the root directory.

1. **Import into Insomnia**:
   - Open Insomnia.
   - Go to `Application > Preferences > Data`.
   - Click `Import Data` > `From File`.
   - Select `manufac_analytics_task_apis.json`.

2. **Test the Endpoints**:
   - Contains requests for `/v1/uuid`, `/v1/async-uuid`, and `/v1/cat`.
   - Set the base URL to `http://localhost:8000/v1` in Insomnia.
   - Send each request to verify responses match the examples above.

- **Docker Note**: In `docker-compose.yml`, `API_BASE_URL` is overridden to `http://backend:8000/v1` for internal networking.

## Docker Configuration

- **Backend**: Runs on port 8000, built from `Dockerfile.backend`.
- **Frontend**: Runs on port 8501, built from `Dockerfile.frontend`.
- **Compose**: Orchestrates both services with a shared `app-network`.

### Running the Project
```bash
docker-compose up --build
```
- Backend: `http://localhost:8000`
- Frontend: `http://localhost:8501`
