from pyrogram import Client, filters
from database.connections import connect_group, disconnect_group, get_all_connections
from database.users import ban_user, unban_user, total_users
from database.movies import get_movie_count
from database.stats import get_global_stats
import config


# CONNECT GROUP
@Client.on_message(filters.command("connect") & filters.user(config.ADMINS))
async def connect_cmd(client, message):

    if message.chat.type == "private":
        return await message.reply("Use this command inside the group.")

    group_id = message.chat.id
    admin_id = message.from_user.id

    await connect_group(group_id, admin_id)

    await message.reply("✅ This group is now connected to the bot.")


# DISCONNECT GROUP
@Client.on_message(filters.command("disconnect") & filters.user(config.ADMINS))
async def disconnect_cmd(client, message):

    if message.chat.type == "private":
        return await message.reply("Use this command inside the group.")

    group_id = message.chat.id

    await disconnect_group(group_id)

    await message.reply("❌ This group has been disconnected.")


# LIST CONNECTIONS
@Client.on_message(filters.command("connections") & filters.user(config.ADMINS))
async def list_connections(client, message):

    groups = await get_all_connections()

    if not groups:
        return await message.reply("No connected groups.")

    text = "🔗 Connected Groups:\n\n"

    for g in groups:
        text += f"`{g}`\n"

    await message.reply(text)


# BOT STATS
@Client.on_message(filters.command("stats") & filters.user(config.ADMINS))
async def stats_cmd(client, message):

    users = await total_users()
    movies = await get_movie_count()
    stats = await get_global_stats()

    text = f"""
📊 Bot Statistics

👤 Total Users: {users}
🎬 Total Movies: {movies}

🔎 Total Searches: {stats.get("total_searches",0)}
📥 Files Served: {stats.get("files_served",0)}
"""

    await message.reply(text)


# BAN USER
@Client.on_message(filters.command("ban") & filters.user(config.ADMINS))
async def ban_cmd(client, message):

    try:
        user_id = int(message.text.split(" ")[1])

        await ban_user(user_id)

        await message.reply(f"🚫 User {user_id} banned.")

    except:
        await message.reply("Usage: /ban user_id")


# UNBAN USER
@Client.on_message(filters.command("unban") & filters.user(config.ADMINS))
async def unban_cmd(client, message):

    try:
        user_id = int(message.text.split(" ")[1])

        await unban_user(user_id)

        await message.reply(f"✅ User {user_id} unbanned.")

    except:
        await message.reply("Usage: /unban user_id")
