# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "thumbhash-python",
#     "tqdm",
# ]
# ///

import json
import thumbhash
from PIL import UnidentifiedImageError
from tqdm import tqdm

with open("list.json", "r") as f:
    imgs = json.load(f)

new_imgs = []

for i in tqdm(imgs):
    with open(i["path"], "rb") as f:
        try:    
            i["thumbhash"] = thumbhash.image_to_thumbhash(f)
        except UnidentifiedImageError:
            print("Error generating thumbhash for", i["path"])
        new_imgs.append(i)

with open("list_v2.json", "w") as f:
    json.dump(new_imgs, f,)
