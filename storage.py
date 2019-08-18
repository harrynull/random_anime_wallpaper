import os.path
import hashlib
import string
import requests
import json

GOOD_CHARS = "-_.() %s%s" % (string.ascii_letters, string.digits)
IMG_LIST_FILE = "list.json"

class storage:
    def sanitize(self, name):
        return ''.join(c for c in name if c in GOOD_CHARS)[:240].replace(' ', '_')
    
    def path(self, src):
        ext = src["img"].split(".")[-1]
        if len(ext)>4 or self.sanitize(ext)!=ext: ext = 'jpg'

        path = "static/" + self.sanitize(src["title"]) + "_" + hashlib.sha1(src["img"].encode()).hexdigest()[0:6] + "." + ext

        # check old filename format
        old_path = "static/" + hashlib.sha1(src["img"].encode()).hexdigest() + "." + ext
        if os.path.isfile(old_path): os.rename(old_path, path)

        # new format
        return path

    def download_img(self, src, path):
        print("Downloading", src, "to", path)
        with open(path, 'wb') as f:
            f.write(requests.get(src).content)
        return src

    def download(self, src):
        path = self.path(src)
        
        if os.path.isfile(path):
            return path
            
        self.download_img(src["img"], path)
        
        if not os.path.isfile(IMG_LIST_FILE):
            with open(IMG_LIST_FILE, "w") as f:
                f.write('[]')
                f.close()

        imgs = json.load(open(IMG_LIST_FILE, "r"))
        src["selected"] = 0
        src["path"] = path
        imgs.append(src)
        with open(IMG_LIST_FILE, "w") as f:
            json.dump(imgs, f)

        return path
    
    def get_list(self):
        return json.load(open(IMG_LIST_FILE, "r"))

    def select(self, path, val):
        imgs = json.load(open(IMG_LIST_FILE, "r"))
        for i in imgs:
            if i["path"] == path:
                i["selected"] = val
                print("selected set.")
                break
        with open(IMG_LIST_FILE, "w") as f:
            json.dump(imgs, f)