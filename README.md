# FastAPI Redis String Concatenation App

This project is a simple web application that lets you concatenate strings and store them in Redis, using a FastAPI backend and a clean HTML frontend.

## Features

- **FastAPI** backend with endpoints to add and retrieve concatenated strings.
- **Redis** used as a fast, in-memory data store.
- **HTML frontend** (`index.html`) for easy interaction.
- **Live UI updates**: The frontend uses JavaScript to send requests to the FastAPI backend and updates the page dynamically with the latest result.
- **Docker-ready** (with `Dockerfile` and `docker_compose.yml`).

## How the UI Updates

The `index.html` file contains JavaScript that listens for user actions (like submitting a string), sends an HTTP request to the FastAPI backend (`/add_string`), and then updates the result area on the page with the response from the server. This provides instant feedback to the user without needing to reload the page.

## Project Structure

```
.
├── main.py              # FastAPI app
├── index.html           # Frontend UI
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build for FastAPI
├── docker_compose.yml   # Docker Compose setup
```

## How to Run

1. **Build and start with Docker Compose:**

   ```sh
   docker-compose -f docker_compose.yml up --build
   ```
2. **Access the app:**

   - Open [http://localhost:8000](http://localhost:8000) to use the frontend.
   - API docs available at [http://localhost:8000/docs](http://localhost:8000/docs).
3. **Stop the app:**

   ```sh
   docker-compose -f docker_compose.yml down
   ```

## API Endpoints

- `POST /add_string` — Add and concatenate a string.
- `GET /get_status` — Get the current concatenated string.

## Requirements

- Docker & Docker Compose (recommended)
- Or: Python 3.8+, FastAPI, Redis, Uvicorn (see `requirements.txt`)

---

**Enjoy concatenating strings with FastAPI and Redis!**
