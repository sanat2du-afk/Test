from pyrogram import Client, filters
from database.mongo import users_col
import config


@Client.on_message(filters.command("broadcast") & filters.user(config.ADMINS))
async def broadcast_cmd(client, message):

    if len(message.command) < 2:
        return await message.reply("Usage:\n/broadcast message")

    text = message.text.split(" ", 1)[1]

    total = 0
    success = 0
    failed = 0

    cursor = users_col.find({})

    async for user in cursor:

        total += 1

        try:
            await client.send_message(
                user["user_id"],
                text
            )
            success += 1

        except:
            failed += 1

    await message.reply(
        f"""
📢 Broadcast Completed

👥 Total Users: {total}
✅ Sent: {success}
❌ Failed: {failed}
"""
    )
