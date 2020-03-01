from bs4 import BeautifulSoup as bs
import requests as r
import pyperclip as clip
from colorama import init, Fore, Back, Style
init()

page = "http://www.torrenttrackerlist.com/torrent-tracker-list"
response = r.get(page)

soup = bs(response.content, "html.parser")

version = soup.find("time", {"class": "entry-time"})
link_box = soup.find("pre", {"class": "prettyprint"})

clip.copy(link_box.text)

print(Fore.WHITE + Back.GREEN + "Torrent trackers from " + version.text + " copied to clipboard!")
print(Style.RESET_ALL)