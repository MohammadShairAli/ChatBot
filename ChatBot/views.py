import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from dotenv import load_dotenv


load_dotenv()
API_URL = "https://api.groq.com/openai/v1/chat/completions" 

def get_chatbot_response(user_input, session):

    if not user_input:
        return {"error": "No user input provided"}


    chat_history = session.get("chat_history", [{"role": "system", "content": (" ").join([
        "you are a helping assistent", 
        "help and remain calmn and pleasing",
        "dont introduce yourself"
        ])}])
    
    chat_history.append({"role": "user", "content": user_input})

    try:
        response = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {os.getenv('GROQ_API')}", "Content-Type": "application/json"},
            json={
                "model": "llama-3.3-70b-versatile",
                "messages": chat_history,
                "max_tokens": 400,
                "temperature": 0.1
            },
        )
        
        data = response.json()
        bot_reply = data.get("choices", [{}])[0].get("message", {}).get("content", "⚠️ No response received.")
        
        chat_history.append({"role": "assistant", "content": (bot_reply)})

        session["chat_history"] = chat_history

        return {"bot_reply": bot_reply}

    except Exception as e:
        return {"error": str(e)}