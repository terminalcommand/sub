import requests

class Downloader:
    USERAGENT = 'SubDB/1.0 (Sub; https://github.com/terminalcommand/sub)'
    HEADERS = {'user-agent': USERAGENT}
    def __init__(self, headers=HEADERS):
        self.headers = headers
    def download(self, url, filename):
        req = requests.get(url, headers = self.headers)
        if req.status_code == 404:
            print("Couldn't find anything.")
        with open(filename, 'wb') as fout:
            print(req.status_code)
            fout.write(req.content)
