from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config


async def check_force_sub(client, user_id):

    try:

        member = await client.get_chat_member(
            config.FORCE_SUB_CHANNEL,
            user_id
        )

        if member.status in ["member", "administrator", "creator"]:
            return True

    except:
        return False

    return False


async def force_sub_message():

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📢 Join Channel",
                    url=f"https://t.me/{config.FORCE_SUB_CHANNEL.replace('@','')}"
                )
            ]
        ]
    )

    text = "⚠️ You must join our channel to download this movie."

    return text, buttons
