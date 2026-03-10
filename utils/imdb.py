import requests

# OMDb API Key (tum apna key config me add kar sakte ho)
OMDB_API = "http://www.omdbapi.com/?apikey=YOUR_API_KEY&t="


async def get_movie_info(movie_name):

    try:
        url = OMDB_API + movie_name
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True":

            return {
                "title": data.get("Title"),
                "year": data.get("Year"),
                "rating": data.get("imdbRating"),
                "poster": data.get("Poster"),
                "genre": data.get("Genre"),
                "plot": data.get("Plot"),
                "cast": data.get("Actors"),
                "release": data.get("Released")
            }

        else:
            return None

    except Exception as e:
        print("IMDB Error:", e)
        return None
