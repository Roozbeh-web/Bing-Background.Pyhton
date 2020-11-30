import requests
import json
import urllib.request
from datetime import datetime

jsonData = json.loads(requests.get(f"https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US").text)

imageUrl = "https://www.bing.com" + jsonData["images"][0]["url"]

today = datetime.today().strftime("%Y-%m-%d")

fullPath = "/home/wabbajack/Pictures/" + today + ".jpg"

urllib.request.urlretrieve(imageUrl,fullPath)