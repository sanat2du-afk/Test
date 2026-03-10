import requests
import config


async def shorten_url(url):

    # Agar shortner disabled hai to original link return
    if not config.URL_SHORTNER or not config.SHORTNER_API:
        return url

    try:

        if config.URL_SHORTNER.lower() == "shareus":

            api = f"https://shareus.in/api?api={config.SHORTNER_API}&url={url}"
            res = requests.get(api).json()

            return res["shortenedUrl"]


        elif config.URL_SHORTNER.lower() == "shrinkme":

            api = f"https://shrinkme.io/api?api={config.SHORTNER_API}&url={url}"
            res = requests.get(api).json()

            return res["shortenedUrl"]


        elif config.URL_SHORTNER.lower() == "adlinkfly":

            api = f"https://adlinkfly.in/api?api={config.SHORTNER_API}&url={url}"
            res = requests.get(api).json()

            return res["shortenedUrl"]


        else:
            return url

    except Exception as e:
        print("Shortner Error:", e)
        return url
