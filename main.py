import asyncio
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest

# Datos preconfigurados (ajusta estos valores)
api_id = 123456  # Reemplazar con tu API ID
api_hash = 'your_api_hash_here'  # Reemplazar con tu API Hash
session_name = 'session'  # Asegúrate de tener session.session ya creado

# Palabras clave para buscar grupos
keywords = ["ganar dinero", "criptomonedas", "trading", "ingresos pasivos", "inversiones", "dólares", "negocio", "emprendimiento", "bitcoin", "ethereum", "binance", "airdrop"]

# Tiempo entre publicaciones
intervalo_minutos = 15

# Mensaje e imagen a publicar
mensaje = "🔥 Descubre cómo generar ingresos desde tu celular. ¡Únete ahora!"
imagen = "promo.jpg"  # Debes subir esta imagen al repositorio

async def publicar_en_grupos():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        await client.start()
        print("Sesión iniciada. Buscando grupos...")

        async for dialog in client.iter_dialogs():
            if dialog.is_group or dialog.is_channel:
                nombre = dialog.name.lower()
                if any(palabra in nombre for palabra in keywords):
                    try:
                        await client.send_file(dialog.id, imagen, caption=mensaje)
                        print(f"Publicado en: {dialog.name}")
                        await asyncio.sleep(intervalo_minutos * 60)
                    except Exception as e:
                        print(f"Error en {dialog.name}: {e}")

if __name__ == "__main__":
    asyncio.run(publicar_en_grupos())