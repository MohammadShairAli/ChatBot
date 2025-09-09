# ChatBot Backend (Django)

## About
A conversational AI backend built with Django and Channels, using the Grok LLaMA-3.3-70B-Versatile model. Easily run locally with Uvicorn.

## Features
- Real-time WebSocket chat
- AI responses powered by LLaMA model
- Session tracking and visitor handling

## Requirements
- Python 3.11+
- Virtual environment (venv)
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/MohammadShairAli/ChatBot.git
   cd ChatBot/Core
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/macOS
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.example.env` to `.env` and add your API key:
   ```
   cp .example.env .env
   ```

## Run
Start the backend server:
```bash
uvicorn Core.asgi:application --reload
```
Open your browser at `http://127.0.0.1:8000/`.

## WebSocket Endpoint
```
ws://127.0.0.1:8000/ws/chat/
```

## Notes
- Use `.env` to store sensitive keys.
- No Redis or Daphne required; uses Uvicorn for ASGI.
- Public repo; avoid putting secret keys directly in the code.
