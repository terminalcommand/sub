import os
import hashlib
import requests
import math
import re
from bs4 import BeautifulSoup

files = os.listdir()
exts = ['.mp4', '.avi', '.mkv', '.mov', '.webm']
useragent = 'SubDB/1.0 (Pyrrot/0.1; http://github.com/jrhames/pyrrot-cli)'
headers = {'user-agent': useragent}


def gen_link(hsh, mode='download'):
    if mode == 'download':
        link = 'http://api.thesubdb.com/?action=download&hash=' + hsh + '&language=en'
    if mode == 'search':
        link = 'http://api.thesubdb.com/?action=search&hash=' + hsh + '&language=en'
    return link

 # this hash function receives the name of the file and returns the hash code


def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()


def search_addicted(name):
    surl = "http://www.addic7ed.com/search.php?search=" + name + "&Submit=Search"
    s = requests.get(surl)
    subregexp = '\/\w+$'
    nurl = re.sub(subregexp, '/1', s.url)
    n = requests.get(nurl)
    soup = BeautifulSoup(n.text, 'html.parser')
    sublinks = []
    sublinks.append(nurl)  # To be used as the referer
    for node in soup.findAll('a', attrs={'class': 'buttonDownload'}):
        sublinks.append('http://www.addic7ed.com' + node['href'])
    return sublinks
for i in files:
    if i[-4:] in exts:
        print("Finding subtitles for: " + i + "\n-> " + get_hash(i))
        r = requests.get(gen_link(get_hash(i)), headers=headers)
        if r.status_code == 404:
            print("Couldn't find anything on SubDB")
            print("Searching at addic7ed")
            addictedlinks = search_addicted(i[:-4])
            print("Downloading from addic7ed")
            ref = addictedlinks[0]
            if len(addictedlinks) < 2:
                print("Couldn't find a subtitle for " + i)
                continue
            r = requests.get(addictedlinks[1], headers={'referer': ref})
        with open(i[:-4] + '.srt', 'wb') as fout:
            fout.write(r.content)
