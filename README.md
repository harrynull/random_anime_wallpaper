# Random Anime Wallpaper API

An API that returns a random anime wallpaper from Reddit [/r/Animewallpaper](https://www.reddit.com/r/Animewallpaper/) with a gallery that can filter unwanted images.

For old version (v1.0.0), see [here](https://gist.github.com/harrynull/0194a5c1119a9c1a3020f3a551559262).

## Documentation

| Endpoint |Key-protected?|Description|
| -------- | ---- | ---- |
| /random_anime_wallpaper | No | Get a random anime wallpaper |
| /update | Yes | Fetch new wallpapers from Reddit |
| /anime_wallpapers | Yes | Get all anime wallpapers, including their status (whether they're filtered). |
| /select | Yes | Filter wallpapers |
| /gallery | Yes | Open the gallery that can filter wallpapers |

You can change the key and decide which endpoint is protected by modifying `random_anime_wallpaper.py`.

## License

All acquired images are copyrighted by their respective authors. **You** are responsible for using these images properly.
The gallery is adapted from [RobinCK/vue-gallery](https://github.com/RobinCK/vue-gallery).
The project itself is licensed under the MIT License.

    MIT License
    
    Copyright (c) 2019 Null
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.