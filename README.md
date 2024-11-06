# ML-Telemetry

This project serves as a platform for telemetry data analysis using machine learning. The application is containerized with Docker, allowing for easy deployment and hot-reloading during development.

## Table of Contents

- [Getting Started](#getting-started)
  - [Download Elysia's Telemetry Data](#download-elysias-telemetry-data)
  - [Running Locally with Docker Compose](#running-locally-with-docker-compose)
  - [Starting the Server for Hot Reloading](#starting-the-server-for-hot-reloading)
- [Accessing the Application](#accessing-the-application)
- [Docker Hub Repository](#docker-hub-repository)

---

## Getting Started

To begin working with the app, clone this repository and ensure you have [Docker](https://www.docker.com/get-started) installed.

### Download Elysia's Telemetry Data

Download historical telemetry data for Elysia from Google Drive:

- [Google Drive - Telemetry Data](https://drive.google.com/drive/folders/1o3RUT3kpWgqgc6GKOip8LYvmVJYf1p8M)

Save the data files locally in the `training_data` folder to ensure they are accessible when running the app.

### Running Locally with Docker Compose

To run the app in a Docker container:

```bash
docker-compose up --build
```

This will build and start the containerized application, exposing it on `http://localhost:8000`.

### Starting the Server for Hot Reloading

Alternatively, to run the app with hot reloading support, use:

```bash
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

This is particularly useful during development, as it reloads the application automatically when changes are detected.

---

## Accessing the Application

Once the app is running, you can access it by navigating to:

- [http://localhost:8000](http://localhost:8000)

---

## Docker Hub Repository

You can pull the application image directly from Docker Hub if you prefer not to build locally:

- [Docker Hub - ML Telemetry](https://hub.docker.com/r/nightofthelivingcarrots512/solarcar-ml)
