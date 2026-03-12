import os

# ==========================
# BASIC BOT CONFIG
# ==========================

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# ==========================
# ADMINS
# ==========================

def get_admins():
    admins = os.getenv("ADMINS", "")
    if admins == "":
        return []
    return [int(admin) for admin in admins.split()]

ADMINS = get_admins()

# ==========================
# DATABASE
# ==========================

DATABASE_URL = os.getenv("DATABASE_URL", "")
DATABASE_NAME = os.getenv("DATABASE_NAME", "moviebot")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "movies")

# ==========================
# CHANNELS
# ==========================

LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))
MOVIE_UPDATE_CHANNEL = int(os.getenv("MOVIE_UPDATE_CHANNEL", "0"))
REQUEST_CHANNEL = int(os.getenv("REQUEST_CHANNEL", "0"))

FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", "")

# ==========================
# FILE CHANNELS (MULTIPLE)
# ==========================

def get_file_channels():
    channels = os.getenv("FILE_CHANNELS", "")
    if channels == "":
        return []
    return [int(ch) for ch in channels.split()]

FILE_CHANNELS = get_file_channels()

# ==========================
# URL SHORTNER
# ==========================

URL_SHORTNER = os.getenv("URL_SHORTNER", "")
SHORTNER_API = os.getenv("SHORTNER_API", "")

# ==========================
# DUMMY PORT (Render Web Service)
# ==========================

DUMMY_PORT = int(os.getenv("DUMMY_PORT", "8080"))

# ==========================
# SETTINGS DEFAULT
# ==========================

IMDB_ENABLED = True
SHORTNER_ENABLED = True
AUTO_DELETE_TIME = 300  # seconds

# ==========================
# BOT INFO
# ==========================

BOT_NAME = os.getenv("BOT_NAME", "Movie AutoFilter Bot")
OWNER_NAME = os.getenv("OWNER_NAME", "Admin")
