# DevOps Profile-Based Model Server

## 🚀 Overview
This project implements a containerized FastAPI-based model server that supports profile-based configuration using environment variables.  
It is designed to be lightweight, modular, and production-ready with clear separation of concerns.

---

## ⚙️ Features
- Profile-based configuration (`PROFILE=throughput`, `quality`, etc.)
- YAML-driven configuration management
- FastAPI REST API
- Dockerized deployment
- CLI tool to list available profiles
- Lightweight and fast build (no heavy ML dependencies)

---

## 📦 Build Docker Image

```bash
docker build -t model-server .
