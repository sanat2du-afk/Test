from pyrogram import Client, filters
from database.movies import add_movie
import config


@Client.on_message(filters.command("addmovie") & filters.user(config.ADMINS))
async def add_movie_command(client, message):

    try:

        args = message.text.split(" ", 4)

        if len(args) < 5:
            return await message.reply(
                "Usage:\n/addmovie movie_name link480 link720 link1080"
            )

        name = args[1]
        link480 = args[2]
        link720 = args[3]
        link1080 = args[4]

        await add_movie(name, link480, link720, link1080)

        await message.reply(
            f"✅ Movie Added Successfully\n\n🎬 {name}"
        )

        # Movie Update Alert
        if config.MOVIE_UPDATE_CHANNEL:

            text = f"""
🎬 New Movie Added

{name}

Available Quality:
• 480p
• 720p
• 1080p
"""

            await client.send_message(
                config.MOVIE_UPDATE_CHANNEL,
                text
            )

    except Exception as e:
        await message.reply(f"Error: {e}")
