# FastAPI Data Tool Lab

Small FastAPI lab for turning Python data-tool logic into API endpoints.

This project demonstrates the basic FastAPI workflow: create endpoints, return JSON responses, use query parameters, accept JSON request bodies, and view everything through automatic Swagger documentation.

## Features

- FastAPI app setup
- Swagger UI at `/docs`
- Basic GET endpoints
- POST endpoint with JSON body
- Query parameter support
- Simple data summary logic
- Separated API routes and helper logic

## Tech Stack

- Python
- FastAPI
- Uvicorn
- JSON

## Project Structure

    fastapi-data-tool-lab/
      src/
        main.py
        summary.py

      README.md
      requirements.txt
      .gitignore

## Installation

Create and activate a virtual environment:

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

Install dependencies:

    pip install -r requirements.txt

## Run

Start the API:

    uvicorn src.main:app --reload

Open Swagger docs:

    http://127.0.0.1:8000/docs

## Endpoints

    GET  /health
    GET  /info
    GET  /report-summary?limit=2
    POST /generate-summary?limit=2

## POST Example Body

    [
      {
        "product_title": "Black Shirt",
        "price": "29.99",
        "sku": "SKU001"
      },
      {
        "product_title": "White Shirt",
        "price": "24.99",
        "sku": "SKU002"
      }
    ]

## Run with Docker

Build the Docker image:

    docker build -t fastapi-data-tool-lab .

Run the container:

    docker run --rm -p 8000:8000 fastapi-data-tool-lab

Open Swagger docs:

    http://127.0.0.1:8000/docs

If port 8000 is already in use, run the container on another local port:

    docker run --rm -p 8001:8000 fastapi-data-tool-lab

Then open:

    http://127.0.0.1:8001/docs
    
## What I Practiced

- Creating a FastAPI application
- Running an API with Uvicorn
- Using Swagger documentation
- Creating GET and POST endpoints
- Working with query parameters
- Accepting JSON request bodies
- Returning structured JSON responses
- Separating API routes from data logic

## Notes

This is a first FastAPI tech-unlock lab, not a production API.

The goal is to understand the core pattern:

    request -> endpoint -> data logic -> JSON response

This pattern can later be used to turn CLI data tools, scrapers, report generators, and automation scripts into small API services.