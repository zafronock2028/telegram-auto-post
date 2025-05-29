from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

# Tu número ya integrado
phone_number = '+584243785498'

# Si alguna vez tienes tu API ID y HASH, los colocas aquí:
api_id = 94575
api_hash = 'a3406de8d171bb422bb6ddf3bbd800e2'

client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    print("✅ Sesión iniciada. Preparando publicación...")

    # Lista de grupos a los que estás unido (muestra solo los públicos y activos)
    dialogs = await client.get_dialogs()
    groups = [d for d in dialogs if d.is_group]

    print("\nGrupos encontrados:")
    for i, group in enumerate(groups):
        print(f"{i+1}. {group.name}")

    selected = input("\n👉 Ingresa los números de los grupos a los que quieres enviar el mensaje (ej: 1,3,5): ")
    indices = [int(x.strip()) - 1 for x in selected.split(",")]
    selected_groups = [groups[i] for i in indices]

    msg = input("\n📝 Escribe el texto a publicar: ")
    img = input("📎 Escribe el nombre del archivo de imagen (o presiona Enter si no hay imagen): ").strip()
    send_image = os.path.exists(img) if img else False

    for group in selected_groups:
        try:
            if send_image:
                await client.send_file(group, img, caption=msg)
            else:
                await client.send_message(group, msg)
            print(f"✅ Mensaje enviado a: {group.name}")
        except Exception as e:
            print(f"⚠️ Error en {group.name}: {e}")

    print("\n✅ Proceso completado.")

with client:
    client.loop.run_until_complete(main())
