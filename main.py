from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import CheckChatInviteRequest
from telethon.tl.functions.contacts import SearchRequest
import asyncio
import time

# Datos de autenticación
api_id = 94575
api_hash = 'a3406de8d171bb422bb6ddf3bbd800e2'
phone_number = '+584243785498'

# Palabras clave en español para encontrar grupos públicos relevantes
keywords = [
    "ganar dinero", "criptomonedas", "ingresos pasivos", "trading", "dinero rápido",
    "negocios online", "marketing digital", "emprendedores", "forex", "airdrop",
    "inversiones", "dinero extra", "multinivel", "trading signals", "bitcoin"
]

# Número máximo de grupos por ronda
max_grupos = 20

client = TelegramClient('session', api_id, api_hash)

async def buscar_grupos(client):
    print("🔍 Buscando grupos con palabras clave relevantes...")
    encontrados = []
    for palabra in keywords:
        print(f"🔎 Buscando: {palabra}")
        resultados = await client(SearchRequest(q=palabra, limit=10))
        for r in resultados.chats:
            if r.username and getattr(r, 'megagroup', False):
                if r.username not in encontrados:
                    encontrados.append(r.username)
        await asyncio.sleep(1)
    print(f"✅ Se encontraron {len(encontrados)} grupos potenciales.")
    return encontrados[:max_grupos]

async def unirse_y_publicar(client, grupos):
    mensaje = input("📝 Escribe el mensaje que deseas enviar: ")
    imagen = input("📎 Ruta del archivo de imagen (deja vacío si no hay): ").strip()

    for username in grupos:
        try:
            print(f"🔗 Uniéndose a: {username}")
            entity = await client.get_entity(username)
            if imagen:
                await client.send_file(entity, imagen, caption=mensaje)
            else:
                await client.send_message(entity, mensaje)
            print(f"✅ Publicado en: {username}")
            await asyncio.sleep(150)  # Espera de 2.5 minutos para evitar spam
        except Exception as e:
            print(f"⚠️ Error en {username}: {e}")

async def main():
    await client.start(phone=phone_number)
    print("🤖 Sesión iniciada.")
    grupos = await buscar_grupos(client)
    if grupos:
        await unirse_y_publicar(client, grupos)
    else:
        print("⚠️ No se encontraron grupos para esta ronda.")

with client:
    client.loop.run_until_complete(main())
