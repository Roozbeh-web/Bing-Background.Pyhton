#import requests module for getting the json file
import requests
#import json module for loading the json file
import json
#import urllib module for getting the image
import urllib.request
#import datetime module for getting the today's date
from datetime import datetime
#import os module for having access to the system
import os


#get and laod the json file and store it in a variable
jsonData = json.loads(requests.get(f"https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US").text)

#store the image url in a variable
imageUrl = "https://www.bing.com" + jsonData["images"][0]["url"]

#store today's date in a variable
today = datetime.today().strftime("%Y-%m-%d")

#store the full path in a variable
fullPath = "/home/wabbajack/Pictures/" + today + ".jpg"

#use urllib module to get the image and save it in defined path
urllib.request.urlretrieve(imageUrl,fullPath)

#use os module to change the background
os.system("gsettings set org.gnome.desktop.background picture-uri file:///" + fullPath)