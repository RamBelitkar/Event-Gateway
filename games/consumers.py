import json
from random import randint
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class BingoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send_numbers()

    async def send_numbers(self):
        sent_numbers = set()
        try:
            while len(sent_numbers) < 100:
                number = randint(1, 100)
                if number not in sent_numbers:
                    sent_numbers.add(number)
                    await self.send(json.dumps({'number': number}))
                    await asyncio.sleep(3)
        except asyncio.CancelledError:
            pass

    async def disconnect(self, close_code):
        pass
