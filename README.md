# 🐳 Docker Infrastructure & Containerization Portfolio

An end-to-end repository showcasing enterprise-grade containerization workflows, Docker management, custom image building, and multi-container orchestration. Built as part of a professional DevOps engineering path with a focus on Red Hat Enterprise Linux (RHEL) standards, security best practices, and reproducible environments.

---

## 🗺️ Portfolio Architecture & Sub-Projects

# Docker-portfolio

​**Flask-app/:** Python/Flask Containerization & Optimization project directory.
​
**Flask-app/app.py:** Multi-route Python Flask application script (/ and /abbas).
​
**Flask-app/Dockerfile:** Layered container build definition and caching configuration.

******************************************************************

**Multi-Stage/:** Secure multi-stage containerization project directory.

**Multi-Stage/Dockerfile:** Production-ready 2-stage build pipeline leveraging slim base images and non-root user security context.

**Multi-Stage/app.py:** Multi-route Python Flask application script (/ and /abbas).

******************************************************************

**Docker-compose/:** Multi-container orchestration project directory.
**Docker-compose/compose.yml:** Orchestration setup defining Nginx web proxy and MySQL database services with isolated custom networking and external volume persistence.

---

## 🛠️ Core Concepts Implemented

* **Deterministic Builds:** Avoiding `latest` tags in production configurations to ensure build reproducibility and stability across environments.
* **Layer Caching Optimization:** Structuring `Dockerfile` instructions (`RUN`, `COPY`, `WORKDIR`) logically to maximize Docker cache utilization and reduce build times.
* **Multi-Stage Build Pipeline:** Utilizing multi-stage builds to decouple build dependencies from the final execution environment, drastically reducing final image footprint and attack surface.
* **Principle of Least Privilege (Security):** Implementing dedicated non-root execution users (USER abbas) within containers to prevent privilege escalation vulnerabilities.
* **Service Orchestration & Dependencies:** Orchestrating multi-container environments using Docker Compose with defined internal networks, static subnets, and volume persistence.
* **Security & Port Binding Isolation:** Restricting container port exposure using explicit host binding (e.g., `-p Host_IP:Host_Port:Container_Port`) to prevent unauthorized network exposure.
* **Custom Networking & Embedded DNS:** Utilizing Custom Bridge Networks (`docker network create`) to enable internal DNS resolution between containers by name instead of volatile IP addresses.

---

## 📂 Featured Projects Breakdown

### 1️⃣ `flask-app` — Lightweight Python Web Microservice

* **Description:** A custom Python/Flask microservice containerized from scratch. Demonstrates environment isolation, pip package management, layered builds, and network interface binding (`Host_IP:5000`).
* **Path:** `./flask-app/`
* **Key Files:** `app.py`, `Dockerfile`

### 2️⃣ Multi-stage — Production-Hardened Multi-Stage Build
Description: An optimized Flask microservice environment utilizing a 2-stage build process. Filters out heavy compilation layers and enforces non-root privilege security (abbas user).
Path: ./Multi-stage/
Key Files: Dockerfile, app.py

### 3️⃣ Docker-compose — Orchestrated Nginx & MySQL Stack
Description: Full-stack infrastructure orchestration linking an Nginx web application with a MySQL database. Features custom subnetting (172.25.0.0/16), explicit service dependency mapping, and persistent volume management.
Path: ./Docker-compose/
Key Files: compose.yml

---

## 🚀 Quick Start Guide

***Docker Engine & Docker-compose**  installed

**Build & Run projects**

```bash
# 1. Single-Stage Flask Application:
cd Flask-app
docker build -t flask-web-app:v1 .
docker run -d -p <Host_IP>:5000:5000 --name flask-service flask-web-app:v1

# 2. Multi-Stage Secure Application:
cd Multi-stage
docker build -t flask-ms:v1 .
docker run -d -p 5000:5000 --name flask-ms flask-ms:v1


# 3. Docker Compose Stack:
cd Docker-compose
docker compose up -d
