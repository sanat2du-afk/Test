from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.users import add_user
import config

START_PIC = "https://files.catbox.moe/nynaku.jpg"


@Client.on_message(filters.command("start"))
async def start_command(client, message):

    user_id = message.from_user.id

    await add_user(user_id)

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🫂 Add Me To Your Group",
                    url=f"https://t.me/{(await client.get_me()).username}?startgroup=true"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔎 Search Movies",
                    url=f"https://t.me/{(await client.get_me()).username}"
                )
            ],
            [
                InlineKeyboardButton(
                    "🎄 About",
                    url="https://t.me/your_about_link"
                )
            ]
        ]
    )

    text = """
🎬 Welcome to Movie AutoFilter Bot

You can search movies easily and get download links with poster and details.

Features:
• Smart Movie Search
• IMDb Poster & Rating
• Multiple Download Quality
• Fast Database Search
"""

    await message.reply_photo(
        photo=START_PIC,
        caption=text,
        reply_markup=buttons
  )
