import time

# User request tracker
user_last_message = {}

# Flood limit (seconds)
FLOOD_TIME = 5


async def check_flood(user_id):

    current_time = time.time()

    if user_id in user_last_message:

        last_time = user_last_message[user_id]

        if current_time - last_time < FLOOD_TIME:
            return True

    user_last_message[user_id] = current_time

    return False
