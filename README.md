# SIAG01

## Overview
SIAG01 is an experimental AI-driven component designed as part of the Signalwoods project.  
The goal of this repository is to develop, version, and evolve an AI agent using professional software engineering best practices.

This repository follows a clean Git-based workflow with clear version history, reproducible setup, and scalable structure.

## Project Objectives
- Build a modular AI agent
- Maintain clean version control from day one
- Enable easy rollback to previous versions
- Support collaborative development
- Follow industry-standard development practices

## Tech Stack
- Python 3.x
- Git & GitHub
- Virtual Environments (`venv`)
- VS Code

## Repository Structure
SIAG01/
├── src/ # Application source code
├── tests/ # Automated tests
├── docs/ # Architecture and design documents
├── scripts/ # Helper scripts
├── .gitignore
├── .env.example
├── README.md
├── requirements.txt

## Getting Started

### Prerequisites
- Python 3.x installed
- Git installed

### Setup
git clone https://github.com/ShuboDey/SIAG01.git
cd SIAG01
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

### How to Run
The standard entry point for the project is `main.py`.
After completing the setup and activating the virtual environment, run:
python src/agent/main.py