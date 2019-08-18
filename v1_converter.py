import json
import requests
import xml.etree.ElementTree
import re
import time
import hashlib
import os.path
import string

RE_EXTRACT_IMG = re.compile(r'<span><a href="(.*?)">\[link\]</a>')

USER_AGENT = "python-backend:tech.harrynull.os_random_anime_wallpaper_converter:1.0.0 (by /u/Harry_Null)"
FEED_URL = "https://www.reddit.com/r/Animewallpaper/search.rss?q=flair_name%3A%22Desktop%22&restrict_sr=1&after={}"
IMG_LIST_FILE = "list.json"

imgs = json.load(open(IMG_LIST_FILE, "r"))
            
last_post = ""
GOOD_CHARS = "-_.() %s%s" % (string.ascii_letters, string.digits)
def sanitize(name):
    return ''.join(c for c in name if c in GOOD_CHARS)[:240].replace(' ', '_')
        
while True:
    e = xml.etree.ElementTree.fromstring(requests.get(FEED_URL.format(last_post), headers={"User-Agent":USER_AGENT}).text.strip())
    for entry in e.findall("{http://www.w3.org/2005/Atom}entry"):
        info = {
            "source": entry.find("{http://www.w3.org/2005/Atom}link").attrib["href"],
            "title":entry.find("{http://www.w3.org/2005/Atom}title").text,
            "img": RE_EXTRACT_IMG.search(entry.find("{http://www.w3.org/2005/Atom}content").text).groups(0)[0] ,
            "id":entry.find("{http://www.w3.org/2005/Atom}id").text
        }
        last_post = info["id"]
        #print(info)
        ext = info["img"].split(".")[-1]
        name = "static/" + hashlib.sha1(info["img"].encode()).hexdigest() + "." + ext
        if os.path.isfile(name):
            new_path = "static/" + sanitize(info["title"]) + "_" + hashlib.sha1(info["img"].encode()).hexdigest()[0:6] + "." + ext
            os.rename(name, new_path)
            info["selected"] = 0
            info["path"] = new_path
            imgs.append(info)
            print("[*] LINKED", info["title"], "to", name)
        else:
            print("[*] MISSED", info["title"])
    
    with open(IMG_LIST_FILE, "w") as f:
        json.dump(imgs, f)
    time.sleep(5)
    print("[*] LAST_POST",last_post)