from pyrogram import Client, filters
from database.movies import delete_movie
import config


@Client.on_message(filters.command("removemovie") & filters.user(config.ADMINS))
async def remove_movie_command(client, message):

    try:

        args = message.text.split(" ", 1)

        if len(args) < 2:
            return await message.reply(
                "Usage:\n/removemovie movie_name"
            )

        name = args[1]

        await delete_movie(name)

        await message.reply(
            f"🗑 Movie Removed Successfully\n\n🎬 {name}"
        )

    except Exception as e:
        await message.reply(f"Error: {e}")
