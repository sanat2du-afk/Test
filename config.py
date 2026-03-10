import os

# Telegram API
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Admins
ADMINS = [int(x) for x in os.getenv("ADMINS_ID", "").split()]

# Database
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME", "MovieBot")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "movies")

# Channels
FILE_CHANNELS = os.getenv("FILE_CHANNELS", "")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))
MOVIE_UPDATE_CHANNEL = int(os.getenv("MOVIE_UPDATE_CHANNEL", 0))
REQUEST_CHANNEL = int(os.getenv("REQST_CHANNEL", 0))

# Force Subscribe
FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL")

# URL Shortner
URL_SHORTNER = os.getenv("URL_SHORTNER")
SHORTNER_API = os.getenv("URLSHORTNER_API")

# Dummy Port (Render)
PORT = int(os.getenv("PORT", 10000))

# Settings Defaults
IMDB_ENABLED = True
SHORTNER_ENABLED = True
AUTO_DELETE_TIME = 300
