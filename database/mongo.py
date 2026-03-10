from motor.motor_asyncio import AsyncIOMotorClient
import config

# MongoDB Client
client = AsyncIOMotorClient(config.DATABASE_URL)

# Database
db = client[config.DATABASE_NAME]

# Collections
movies_col = db[config.COLLECTION_NAME]
users_col = db["users"]
stats_col = db["stats"]
connections_col = db["connections"]
requests_col = db["requests"]

async def init_db():
    """
    Initialize database indexes
    """

    # Movie name search index
    await movies_col.create_index("name")

    # User ID index
    await users_col.create_index("user_id")

    # Group connections index
    await connections_col.create_index("group_id")

    # Request index
    await requests_col.create_index("movie")

    print("MongoDB Connected Successfully")
