from pyrogram import Client, filters
import config

settings = {
    "imdb": True,
    "shortner": False,
    "autodelete": 300
}


# SHOW SETTINGS
@Client.on_message(filters.command("settings") & filters.user(config.ADMINS))
async def show_settings(client, message):

    text = f"""
⚙ Bot Settings

🎬 IMDb Info: {"ON" if settings["imdb"] else "OFF"}
🔗 URL Shortner: {"ON" if settings["shortner"] else "OFF"}
🧹 Auto Delete: {settings["autodelete"]} seconds
"""

    await message.reply(text)


# IMDB TOGGLE
@Client.on_message(filters.command("imdb") & filters.user(config.ADMINS))
async def imdb_toggle(client, message):

    settings["imdb"] = not settings["imdb"]

    status = "ON" if settings["imdb"] else "OFF"

    await message.reply(f"IMDb Info turned {status}")


# SHORTNER TOGGLE
@Client.on_message(filters.command("shortner") & filters.user(config.ADMINS))
async def shortner_toggle(client, message):

    settings["shortner"] = not settings["shortner"]

    status = "ON" if settings["shortner"] else "OFF"

    await message.reply(f"URL Shortner turned {status}")


# AUTO DELETE CHANGE
@Client.on_message(filters.command("autodelete") & filters.user(config.ADMINS))
async def autodelete_cmd(client, message):

    try:

        seconds = int(message.text.split(" ")[1])

        settings["autodelete"] = seconds

        await message.reply(f"Auto delete set to {seconds} seconds")

    except:
        await message.reply("Usage: /autodelete seconds")
