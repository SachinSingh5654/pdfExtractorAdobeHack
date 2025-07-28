# Adobe India Hackathon: Connecting the Dots

## Project Overview

This project reimagines PDFs as intelligent, interactive documents that understand structure, surface insights, and respond like a trusted research companion. It consists of:

1. **Backend**: A PDF processing service that extracts structured outlines (Round 1A)
2. **Frontend**: An interactive webapp for enhanced PDF reading (Round 2)

## Features

### Backend (Round 1A)
- Extracts document title and hierarchical headings (H1, H2, H3)
- Processes PDFs up to 50 pages in under 10 seconds
- Outputs clean JSON with page numbers
- Runs in a Docker container with no internet dependency

### Frontend (Round 2)
- Interactive PDF viewer with Adobe's PDF Embed API
- Document outline/sidebar navigation
- Responsive design for optimal reading
- Document management interface

## System Architecture
adobe-hackathon/
├── backend/ # PDF processing service
│ ├── Dockerfile # Container configuration
│ ├── requirements.txt # Python dependencies
│ ├── app.py # Main application
│ ├── pdf_processor.py # PDF processing logic
├── frontend/ # Web application
│ ├── public/ # Static assets
│ ├── src/ # React components
│ ├── server.js # Express server
├── README.md # This documentation




## Prerequisites

- Docker
- Node.js (v16+)
- Python (for local backend testing)

## Installation

### Backend Setup

1. Build the Docker image:
   ```bash
   cd backend
   docker build --platform linux/amd64 -t pdf-outline-extractor:latest .

## Run the container:
docker run --rm -v ${PWD}/input:/app/input -v ${PWD}/output:/app/output --network none pdf-outline-extractor:latest



Select a document from the sidebar

Use the outline to navigate through the document

Interact with the PDF using Adobe's embedded viewer tools
