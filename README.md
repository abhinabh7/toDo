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


todo-app-flask/
│
├─ app.py # Flask application
├─ requirements.txt # Python dependencies
├─ Dockerfile # Docker build instructions
├─ docker-compose.yml # Compose file for local deployment
├─ .github/workflows/ # GitHub Actions workflow
│ └─ ci.yml
├─ static/ # CSS/JS files
└─ templates/ # HTML templates


---

## Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/abhinabh7/toDo.git
cd todo-app-flask
2️⃣ Build Docker image locally (optional)
docker build -t todo-app .
docker run -p 5000:5000 todo-app

Visit http://localhost:5000 to see the app.

3️⃣ CI/CD with GitHub Actions

Workflow located at .github/workflows/ci.yml

Automatically builds and pushes Docker image to Docker Hub whenever you push code to main.

Workflow steps:

Checkout repository code

Log in to Docker Hub using secrets (DOCKER_USERNAME and DOCKER_PASSWORD)

Build Docker image

Push image to Docker Hub

4️⃣ Deployment with Docker Compose

Ensure docker-compose.yml is present:

version: '3'
services:
  web:
    image: abhinabh/todo-app:latest
    ports:
      - "5000:5000"

Pull latest image and run:

docker compose pull
docker compose up -d

Access app at http://localhost:5000

Automatically pulls the latest Docker image from Docker Hub.

5️⃣ GitHub Secrets Setup

For CI/CD workflow, create the following repository secrets:

Secret Name	Value
DOCKER_USERNAME	your Docker Hub username
DOCKER_PASSWORD	your Docker Hub Personal Access Token
6️⃣ Notes

The Docker Hub image is public, so anyone can pull it with:

docker pull abhinabh/todo-app:latest

CI/CD pipeline ensures any code changes are automatically reflected in the Docker image.

Local deployment via Docker Compose ensures you can test the latest version easily.

7️⃣ Future Enhancements

Make Docker Hub image private (optional).

Deploy the app to cloud servers (AWS, Azure, DigitalOcean, etc.).

Add automated testing in the CI/CD workflow.

Add database persistence (currently the app is in-memory).

Author

Abhinabh – DevOps Beginner Project


---

You can copy everything above, **paste it into your `README.md`**, save, and push it to GitHub.  

If you want, I can **also add some badges** (build status, Docker Hub pulls) to make it look **more professional for your portfolio**.  

Do you want me to do that next?
