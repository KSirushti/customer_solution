# Fin360 – Customer 360 Data Product Designer with Agentic AI

Fin360 is a full-stack, AI-driven platform that automates the design and certification of Customer 360 data products. It utilizes a modular multi-agent architecture powered by on-premise LLMs (via Ollama), enabling seamless schema generation, source mapping, transformation logic creation, data flow configuration, and product certification. The system offers a complete no-code experience through a modern React-Django interface.

## Problem Statement

Designing data products such as Customer 360 in domains like retail banking typically involves manual coordination across teams, domain knowledge, and extensive time investment. These challenges result in inefficiencies, inconsistent data design practices, and delayed deployment. Fin360 addresses these limitations by using intelligent agents to automate each stage of the data product lifecycle.

## Solution Overview

The platform is based on a sequence of specialized agents, each responsible for a key function:

- The Design Agent interprets business use cases and generates structured schemas.
- The Source Discovery Agent identifies relevant source attributes and systems.
- The Mapping Agent builds field-level transformation logic from source to target.
- The Flow Agent defines ingress, egress, and storage configurations.
- The Certification Agent validates schema quality, structure, and compliance.

Each agent is powered by on-premise language models and accessed via dedicated REST APIs. Results are orchestrated within a user-friendly interface that guides users step-by-step through the data product creation pipeline.

## Technologies Used

- Frontend: React.js, Axios, CSS
- Backend: Django, Django REST Framework
- Agents: Python-based logic modules with REST endpoints
- LLM: Mistral model served via Ollama
- Embedding Models: Ollama-based semantic similarity tools
- Database: SQLite for metadata and intermediate storage

## Setup Instructions

1. Run the Django backend:
   - Navigate to the customer360-backend directory
   - Run python manage.py runserver

2. Start the Ollama LLM service:
   - Run ollama run mistral in a separate terminal

3. Launch the React frontend:
   - Navigate to customer360-frontend
   - Run npm install followed by npm start

## Demo Workflow

The application guides the user through the following stages:

1. Welcome screen with use case context  
2. Schema generation using the design agent  
3. Source mapping using semantic matching  
4. Transformation mapping and logic generation  
5. Ingress and egress flow definition  
6. Final certification and output validation

## Key Features

- Modular multi-agent system powered by on-prem LLMs  
- REST API interfaces for each agent  
- Interactive UI for end-to-end data product design  
- Fully local and privacy-preserving architecture  
- Adaptable to multiple enterprise domains  

## Status

- Functional prototype implemented and tested  
- Supports generation and mapping of 10,000+ customer records  
- Ready for extension and integration in enterprise data pipelines  

## Authors

- Team SuperNova  
