from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import asyncio
import os

# Pedir API info solo una vez y guardar la sesión
api_id = 123456  # Cambia esto en Render
api_hash = 'your_api_hash_here'  # Cambia esto en Render
session_name = 'session'

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start()
    print("✅ Sesión iniciada con éxito.")

    # Leer grupos donde el usuario ya está
    dialogs = await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=100,
        hash=0
    ))

    groups = [d for d in dialogs.chats if getattr(d, 'megagroup', False)]
    print("\nGrupos disponibles:")
    for i, group in enumerate(groups):
        print(f"{i+1}. {group.title}")

    choices = input("\n📌 Escribe los números de los grupos separados por coma donde quieres publicar (ej: 1,3,5): ")
    selected_indices = [int(x.strip())-1 for x in choices.split(',')]
    selected_groups = [groups[i] for i in selected_indices]

    # Texto del mensaje
    message = input("\n📝 Escribe el texto del mensaje que quieres enviar: ")

    # Imagen (opcional)
    image_path = input("📎 Escribe el nombre del archivo de imagen (o deja vacío si no quieres enviar imagen): ").strip()
    send_image = os.path.exists(image_path) if image_path else False

    print("\n🚀 Enviando mensaje...")
    for group in selected_groups:
        try:
            if send_image:
                await client.send_file(group, image_path, caption=message)
            else:
                await client.send_message(group, message)
            print(f"✅ Enviado a: {group.title}")
            await asyncio.sleep(5)  # Espera entre envíos
        except Exception as e:
            print(f"⚠️ Error en {group.title}: {e}")

    print("\n🏁 Publicación completada.")

with client:
    client.loop.run_until_complete(main())
