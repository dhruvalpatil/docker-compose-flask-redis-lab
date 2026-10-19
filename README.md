# Docker Compose: Flask + Redis Visit Counter

## Overview

A hands-on DevOps project demonstrating how to build and run a multi-container application using Docker Compose. A Flask web application communicates with Redis to maintain a page-visit counter.

## Architecture

- **Flask:** Handles HTTP requests and displays the visit counter.
- **Redis:** Stores the counter using the `page_visits` key.
- **Docker Compose:** Builds and manages both services.
- **Custom configuration:** Uses the `REDIS_HOST` environment variable for service discovery.
- **Health check:** Redis health status is checked before the web service starts.
- **Persistent storage:** A named volume, `redis-data`, stores Redis data under `/data`.
- **Port mapping:** Host port `5001` maps to Flask container port `5000`.

## Project Structure

```text
docker-compose-lab/
├── app.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .gitignore
└── README.md
```

## Prerequisites

- Docker Desktop
- Docker Compose
- A web browser

## Run the Application

Start and build the services:

```bash
docker compose up -d --build
```

Check service status:

```bash
docker compose ps
```

Open the application:

`http://localhost:5001`

Refresh the page to increase the visit counter.

## Health Check

Open:

`http://localhost:5001/health`

Expected response:

```json
{"status": "healthy"}
```

## Useful Commands

```bash
# View service status
docker compose ps

# View application logs
docker compose logs web

# View Redis logs
docker compose logs redis

# Read the current counter
docker compose exec redis redis-cli GET page_visits

# Recreate the Flask service
docker compose up -d --force-recreate web

# Stop and remove containers and the Compose network
docker compose down
```

## Key DevOps Concepts

- Multi-container orchestration with Docker Compose
- Container networking and service-name DNS
- Environment-variable configuration
- Health checks and service dependencies
- Named volumes and data persistence
- Container logs and troubleshooting

## Cleanup Note

`docker compose down` preserves the named volume by default. To remove the Redis data volume as well, use `docker compose down -v` only when you intentionally want to delete the saved lab data.

## Learning Outcome

Built and tested a containerized Flask + Redis application, configured inter-service communication and health checks, and practiced container lifecycle management and persistent storage.
