from pyrogram import Client, filters
from pyrogram.types import Message

import asyncio

from settings import API_ID, API_HASH
from data_validate import validate

app = Client("my_session", API_ID, API_HASH)

@app.on_message(filters=filters.text)
async def start(client: Client, message: Message):
    if message.text == "/start":
        with open("username_source.txt", "r") as users:
            for user in users:
                await client.add_chat_members(chat_id=message.chat.id, user_ids=await validate(user))
                await asyncio.sleep(1)

app.run()