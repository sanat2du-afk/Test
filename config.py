import os

# Telegram API
API_ID = int(os.getenv("28473056"))
API_HASH = os.getenv("65dd11a5bed33d2b43c997e4cbc3dee2")
BOT_TOKEN = os.getenv("8045819879:AAG-Z205mYi0m6Fr1kYGdJv7c1P74ssUatA")

# Admins
ADMINS = [int(x) for x in os.getenv("ADMINS_ID", "8078089503").split()]

# Database
DATABASE_URL = os.getenv("mongodb+srv://rinamurmu231:rinamurmu231@badsha.xp8bc.mongodb.net")
DATABASE_NAME = os.getenv("DATABASE_NAME", "MovieBot")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "movies")

# Channels
FILE_CHANNELS = os.getenv("FILE_CHANNELS", "-1003813092378")
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
SHORTNER_ENABLED = False
AUTO_DELETE_TIME = 300
