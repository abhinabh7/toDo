# To-Do App (Flask + Docker + CI/CD)

A simple **To-Do List application** built with Python Flask, Dockerized, and deployed using **CI/CD** with GitHub Actions.  
This project demonstrates **DevOps practices** for beginners: version control, containerization, CI/CD pipelines, and local deployment with Docker Compose.

---

## Project Overview

- Build a Flask-based To-Do application.
- Containerize the app with Docker.
- Push Docker images to **Docker Hub** automatically via **GitHub Actions**.
- Deploy the app locally using **Docker Compose**.

---

## Tech Stack

- **Backend:** Python Flask  
- **Containerization:** Docker  
- **CI/CD:** GitHub Actions  
- **Registry:** Docker Hub  
- **Deployment:** Docker Compose (local)

---

## Project Structure

```
todo-app-flask/
│
├─ app.py                # Flask application
├─ requirements.txt      # Python dependencies
├─ Dockerfile            # Docker build instructions
├─ docker-compose.yml    # Compose file for local deployment
├─ .github/workflows/    # GitHub Actions workflow
│   └─ ci.yml
├─ static/               # CSS/JS files
└─ templates/            # HTML templates
```

---

## CI/CD Architecture

![CI/CD Pipeline Diagram](./1773162465446_image.png)

The workflow follows 4 steps:

1. **Code Changes & Push** – Developer writes code locally and pushes to GitHub.
2. **Trigger GitHub Actions** – Push to `main` triggers the CI/CD pipeline (Checkout → Build Docker Image → Push to Docker Hub).
3. **Pull Latest Image** – Docker Compose pulls the latest image (`abhinabh/todo-app:latest`) from Docker Hub.
4. **Deploy & Update** – App is served locally via Docker Compose at `http://localhost:5000`.

---

## Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/abhinabh7/toDo.git
cd todo-app-flask
```

### 2️⃣ Build Docker image locally (optional)

```bash
docker build -t todo-app .
docker run -p 5000:5000 todo-app
```

Visit `http://localhost:5000` to see the app.

---

### 3️⃣ CI/CD with GitHub Actions

- Workflow located at `.github/workflows/ci.yml`
- Automatically builds and pushes Docker image to Docker Hub whenever you push code to `main`.

**Workflow steps:**
1. Checkout repository code
2. Log in to Docker Hub using secrets (`DOCKER_USERNAME` and `DOCKER_PASSWORD`)
3. Build Docker image
4. Push image to Docker Hub

---

### 4️⃣ Deployment with Docker Compose

Ensure `docker-compose.yml` is present:

```yaml
version: '3'
services:
  web:
    image: abhinabh/todo-app:latest
    ports:
      - "5000:5000"
```

Pull the latest image and run:

```bash
docker compose pull
docker compose up -d
```

- Access app at `http://localhost:5000`
- Automatically pulls the latest Docker image from Docker Hub.

---

### 5️⃣ GitHub Secrets Setup

For the CI/CD workflow, create the following repository secrets:

| Secret Name       | Value                              |
|-------------------|------------------------------------|
| `DOCKER_USERNAME` | Your Docker Hub username           |
| `DOCKER_PASSWORD` | Your Docker Hub Personal Access Token |

---

### 6️⃣ Notes

- The Docker Hub image is public, so anyone can pull it with:

```bash
docker pull abhinabh/todo-app:latest
```

- CI/CD pipeline ensures any code changes are automatically reflected in the Docker image.
- Local deployment via Docker Compose ensures you can test the latest version easily.

---

### 7️⃣ Future Enhancements

- Make Docker Hub image private (optional).
- Deploy the app to cloud servers (AWS, Azure, DigitalOcean, etc.).
- Add automated testing in the CI/CD workflow.
- Add database persistence (currently the app is in-memory).

---

## Author

**Abhinabh** – DevOps Beginner Project
