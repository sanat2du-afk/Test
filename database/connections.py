from database.mongo import connections_col

# Connect Group
async def connect_group(group_id, owner_id):

    data = {
        "group_id": group_id,
        "owner_id": owner_id,
        "active": True
    }

    await connections_col.update_one(
        {"group_id": group_id},
        {"$set": data},
        upsert=True
    )


# Disconnect Group
async def disconnect_group(group_id):

    await connections_col.update_one(
        {"group_id": group_id},
        {"$set": {"active": False}}
    )


# Check If Group Connected
async def is_group_connected(group_id):

    group = await connections_col.find_one({"group_id": group_id})

    if group and group.get("active"):
        return True

    return False


# Get All Connected Groups
async def get_all_connections():

    groups = []

    cursor = connections_col.find({"active": True})

    async for group in cursor:
        groups.append(group["group_id"])

    return groups


# Remove Group Completely
async def remove_group(group_id):

    await connections_col.delete_one({"group_id": group_id})
