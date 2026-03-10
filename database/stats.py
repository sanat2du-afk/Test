from datetime import datetime
from database.mongo import stats_col

# Increase Total Searches
async def increase_search_count():

    await stats_col.update_one(
        {"_id": "global"},
        {"$inc": {"total_searches": 1}},
        upsert=True
    )


# Increase Files Served
async def increase_files_served():

    await stats_col.update_one(
        {"_id": "global"},
        {"$inc": {"files_served": 1}},
        upsert=True
    )


# Increase Daily Search
async def increase_daily_search():

    today = datetime.utcnow().strftime("%Y-%m-%d")

    await stats_col.update_one(
        {"date": today},
        {"$inc": {"searches": 1}},
        upsert=True
    )


# Get Global Stats
async def get_global_stats():

    data = await stats_col.find_one({"_id": "global"})

    if not data:
        return {
            "total_searches": 0,
            "files_served": 0
        }

    return data


# Get Daily Stats
async def get_daily_stats():

    today = datetime.utcnow().strftime("%Y-%m-%d")

    data = await stats_col.find_one({"date": today})

    if not data:
        return {"searches": 0}

    return data
