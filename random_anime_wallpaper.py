# MIT License
# 
# Copyright (c) 2019 Null
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import random
import os.path
import copy
from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file
from crawler import crawler
from storage import storage
from functools import wraps

app = Flask(__name__)

URL_BASE_PATH = "http://127.0.0.1:5000/"
KEY = ""

crawler = crawler()
storage = storage()

def key_protected(func):
    @wraps(func)
    def wrapper():
        json = request.get_json()
        if KEY == "" or request.args.get('key', '') == KEY or (json and 'key' in json and json['key'] == KEY):
            return func()
        else:
            return jsonify({"error":"403","reason":"This operation is key-protected. Please provide a correct key."})
            
    return wrapper

@app.route("/random_anime_wallpaper")
def random_anime_wallpaper():
    res = storage.get_list()
    while True:
        choice = res[random.randint(0, len(res)-1)]
        print(choice)
        if choice["selected"] >=0: break
    
    selected = copy.deepcopy(choice)
    if request.args.get('download', False):
        selected["img_src"] = selected["img"]
        selected["img"] = URL_BASE_PATH + storage.download(selected)
    return jsonify(selected)
    
@app.route("/update")
@key_protected
def update():
    for i in crawler.fetch_feed():
        storage.download(i)
    return 'ok'
    
@app.route("/anime_wallpapers")
@key_protected
def all_anime_wallpapers():
    return jsonify(storage.get_list())
    
@app.route("/select", methods=['POST'])
@key_protected
def select():
    r=request.get_json(silent=True)
    storage.select(r["name"], r["val"])
    return 'ok'

@app.route("/gallery")
def gallery():
    return send_file("gallery/gallery.html")
