import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .views import get_chatbot_response
import asyncio  

class ChatConsumer(AsyncWebsocketConsumer):
    chat_histories = {'data': []}

    async def connect(self):
        await self.accept()
        print("WebSocket connected.")

    async def disconnect(self, close_code):
        print(f"WebSocket disconnected: {close_code}")

    async def receive(self, text_data):
        try:
            self.chat_histories['data'].append({"role": "user", "content": text_data})
            response_data = await asyncio.to_thread(get_chatbot_response, text_data, self.chat_histories)
            reply = response_data.get("bot_reply", "Sorry, I didn't understand that.")
            self.chat_histories['data'].append({"role": "assistant", "content": reply})
            await self.send(text_data=json.dumps(reply))

        except Exception as e:
            error_message = (f"Error processing message: {str(e)}")
            await self.send(text_data=json.dumps({"error": error_message}))
