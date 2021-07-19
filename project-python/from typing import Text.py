from typing import Text
import webbrowser
import json
from urllib.request import urlopen

print("Let`s find an old website.")
site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 2021.05.31: ")
url = "facebook.com" % (site, era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.load(text)
try:
    old_site = data["archived_snapshots"]["closest"]['url']
    print("found this copy: ", old_site)
    print("it should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)