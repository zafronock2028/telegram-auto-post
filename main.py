import asyncio
from telethon.sync import TelegramClient

api_id = 12345678  # Reemplazar con tu API ID
api_hash = 'your_api_hash'  # Reemplazar con tu API HASH
phone = '+584243785498'

async def main():
    async with TelegramClient('session', api_id, api_hash) as client:
        me = await client.get_me()
        print(f"Sesión iniciada como: {me.first_name}")

asyncio.run(main())
