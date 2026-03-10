import asyncio
from pyrogram import Client
from flask import Flask
from threading import Thread

import config

# Pyrogram Bot Client
bot = Client(
    "AdvancedAutoFilterBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

# Dummy Flask App (Render Web Service ke liye)
app = Flask(__name__)

@app.route("/")
def home():
    return "Advanced AutoFilter Bot is Running 🚀"


def run_web():
    app.run(host="0.0.0.0", port=config.PORT)


async def start_bot():
    await bot.start()
    print("Bot Started Successfully")

    me = await bot.get_me()
    print(f"Logged in as {me.first_name}")

    await asyncio.Event().wait()


if __name__ == "__main__":

    # Flask Server Thread
    t = Thread(target=run_web)
    t.start()

    # Start Telegram Bot
    asyncio.run(start_bot())
