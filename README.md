# DevOps Profile-Based Model Server

## 🚀 Overview
This project implements a containerized FastAPI-based model server that supports profile-based configuration using environment variables.

---

## ⚙️ Features
- Profile-based configuration (`PROFILE=throughput`, `quality`, etc.)
- YAML-driven config
- FastAPI REST API
- Dockerized deployment
- CLI to list profiles

---

## 📦 Build Docker Image

```bash
docker build -t model-server .