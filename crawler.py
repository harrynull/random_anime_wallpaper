import xml.etree.ElementTree
import requests
import re
import time

# See https://github.com/reddit-archive/reddit/wiki/API for UserAgent format
USER_AGENT = "python-backend:tech.harrynull.os_random_anime_wallpaper:1.1.0 (by /u/Harry_Null)"
CACHE_VALID_TIME = 60 * 10 # 10mins

RE_EXTRACT_IMG = re.compile(r'<span><a href="(.*?)">\[link\]</a>')
FEED_URL = "https://www.reddit.com/r/Animewallpaper/search.rss?q=flair_name%3A%22Desktop%22&restrict_sr=1"

class crawler:
    def _entry_to_dictionary(self, entry):
        return {
            "source": entry.find("{http://www.w3.org/2005/Atom}link").attrib["href"],
            "title":entry.find("{http://www.w3.org/2005/Atom}title").text,
            "img": RE_EXTRACT_IMG.search(entry.find("{http://www.w3.org/2005/Atom}content").text).groups(0)[0] 
        }

    last_fetch_time = 0
    cached_results = None

    def fetch_feed(self):
        # Use cache if still valid
        if time.time() - self.last_fetch_time <= CACHE_VALID_TIME and self.cached_results:
            return self.cached_results
        
        results = []
        e = xml.etree.ElementTree.fromstring(requests.get(FEED_URL, headers={"User-Agent":USER_AGENT}).text.strip())
        for entry in e.findall("{http://www.w3.org/2005/Atom}entry"):
            try:
                res = self._entry_to_dictionary(entry)
                if 'v.redd.it' in res['img']: continue
                results.append(res)
            except:
                pass
                
        cached_results = results
        last_fetch_time = time.time()
        return results
