from database.mongo import movies_col
from utils.fuzzy_search import similar_movies

# Add Movie
async def add_movie(name, link480=None, link720=None, link1080=None):

    movie = name.lower()

    data = {
        "name": movie,
        "link480": link480,
        "link720": link720,
        "link1080": link1080
    }

    await movies_col.insert_one(data)


# Remove Movie
async def delete_movie(name):

    movie = name.lower()

    await movies_col.delete_one({"name": movie})


# Search Movie
async def search_movie(name):

    movie = name.lower()

    result = await movies_col.find_one({"name": {"$regex": movie}})

    return result


# Movie Count
async def get_movie_count():

    count = await movies_col.count_documents({})

    return count


# Remove Duplicate Movies
async def remove_duplicates():

    seen = set()
    cursor = movies_col.find({})

    async for movie in cursor:

        name = movie["name"]

        if name in seen:
            await movies_col.delete_one({"_id": movie["_id"]})
        else:
            seen.add(name)


# Get All Movie Names (for fuzzy search)
async def get_all_movie_names():

    names = []

    cursor = movies_col.find({}, {"name": 1})

    async for doc in cursor:
        names.append(doc["name"])

    return names


# Related Movie Suggestions
async def related_movies(query):

    movies = await get_all_movie_names()

    suggestions = similar_movies(query, movies)

    return suggestions
