# 🐳 Docker Infrastructure & Containerization Portfolio

An end-to-end repository showcasing enterprise-grade containerization workflows, Docker management, custom image building, and multi-container orchestration. Built as part of a professional DevOps engineering path with a focus on Red Hat Enterprise Linux (RHEL) standards, security best practices, and reproducible environments.

---

## 🗺️ Portfolio Architecture & Sub-Projects

Docker-portfolio/
│
├── 01-flask-web-app/             # Python/Flask Containerization & Optimization
│   ├── app.py                    # Multi-route Python Flask Application
│   ├── Dockerfile                # Layered container build definition
│   └── README.md                 # Project-specific execution instructions
│
└── README.md                     # Main Portfolio Documentat
---

## 🛠️ Core Concepts Implemented

* **Deterministic Builds:** Avoiding `latest` tags in production configurations to ensure build reproducibility and stability across environments.
* **Layer Caching Optimization:** Structuring `Dockerfile` instructions (`RUN`, `COPY`, `WORKDIR`) logically to maximize Docker cache utilization and reduce build times.
* **Security & Port Binding Isolation:** Restricting container port exposure using explicit host binding (e.g., `-p Host_IP:Host_Port:Container_Port`) to prevent unauthorized network exposure.
* **Custom Networking & Embedded DNS:** Utilizing Custom Bridge Networks (`docker network create`) to enable internal DNS resolution between containers by name instead of volatile IP addresses.

---

## 📂 Featured Projects Breakdown

### 1️⃣ `flask-app` — Lightweight Python Web Microservice

* **Description:** A custom Python/Flask microservice containerized from scratch. Demonstrates environment isolation, pip package management, layered builds, and network interface binding (`Host_IP:5000`).
* **Path:** `./flask-app/`
* **Key Files:** `app.py`, `Dockerfile`
---

## 🚀 Quick Start Guide

***Docker Engine**  installed

**Build & Run Projects (e.g., Flask Application)**

# Build the Docker Image
docker build -t flask-web-app:v1 .

# Run Container in Detached Mode
docker run -d -p <Host_IP>:5000:5000 --name flask-service flask-app:v1
