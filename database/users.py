from database.mongo import users_col

# Add User
async def add_user(user_id):

    user = await users_col.find_one({"user_id": user_id})

    if not user:

        data = {
            "user_id": user_id,
            "banned": False,
            "search_count": 0
        }

        await users_col.insert_one(data)


# Get User
async def get_user(user_id):

    return await users_col.find_one({"user_id": user_id})


# Total Users
async def total_users():

    count = await users_col.count_documents({})

    return count


# Ban User
async def ban_user(user_id):

    await users_col.update_one(
        {"user_id": user_id},
        {"$set": {"banned": True}}
    )


# Unban User
async def unban_user(user_id):

    await users_col.update_one(
        {"user_id": user_id},
        {"$set": {"banned": False}}
    )


# Check Ban
async def is_banned(user_id):

    user = await users_col.find_one({"user_id": user_id})

    if user and user.get("banned"):
        return True

    return False


# Increase Search Count
async def increase_search(user_id):

    await users_col.update_one(
        {"user_id": user_id},
        {"$inc": {"search_count": 1}}
         )
