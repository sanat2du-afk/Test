from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from database.movies import search_movie, related_movies
from database.users import increase_search
from database.stats import increase_search_count, increase_daily_search, increase_files_served
from utils.imdb import get_movie_info
from utils.shortner import shorten_url
from utils.antiflood import check_flood
from utils.force_sub import check_force_sub, force_sub_message

import config


@Client.on_message(filters.text & filters.group)
async def search_movies(client, message):

    user_id = message.from_user.id
    query = message.text.strip()

    # Flood Protection
    flood = await check_flood(user_id)
    if flood:
        return await message.reply("⚠️ Slow down! Too many requests.")

    await increase_search(user_id)
    await increase_search_count()
    await increase_daily_search()

    movie = await search_movie(query)

    if movie:

        info = await get_movie_info(query)

        link480 = movie.get("link480")
        link720 = movie.get("link720")
        link1080 = movie.get("link1080")

        if config.URL_SHORTNER:
            if link480:
                link480 = await shorten_url(link480)
            if link720:
                link720 = await shorten_url(link720)
            if link1080:
                link1080 = await shorten_url(link1080)

        buttons = []

        row = []

        if link480:
            row.append(InlineKeyboardButton("📥 480p", url=link480))

        if link720:
            row.append(InlineKeyboardButton("📥 720p", url=link720))

        if link1080:
            row.append(InlineKeyboardButton("📥 1080p", url=link1080))

        if row:
            buttons.append(row)

        reply_markup = InlineKeyboardMarkup(buttons)

        caption = f"""
🎬 {info['title']}

⭐ IMDb Rating: {info['rating']}
📅 Release Date: {info['release']}
🎭 Cast: {info['cast']}
🏷 Genre: {info['genre']}

📝 {info['plot']}
"""

        await increase_files_served()

        await message.reply_photo(
            photo=info["poster"],
            caption=caption,
            reply_markup=reply_markup
        )

    else:

        suggestions = await related_movies(query)

        if suggestions:

            buttons = [
                [InlineKeyboardButton(movie.title(), callback_data=f"search_{movie}")]
                for movie in suggestions
            ]

            await message.reply(
                "🚫 Movie Not Found\n\nDid you mean:",
                reply_markup=InlineKeyboardMarkup(buttons)
            )

        else:

            await client.send_message(
                config.REQUEST_CHANNEL,
                f"📥 Movie Request:\n{query}\n\nUser: {message.from_user.id}"
            )

            await message.reply(
                "🚫 Movie not found.\n\nYour request has been sent to admin."
      )
