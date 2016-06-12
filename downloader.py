#import http.client
import urllib3

class Downloader:
    USERAGENT = 'SubDB/1.0 (Sub; https://github.com/terminalcommand/sub)'
    HEADERS = {'user-agent': USERAGENT, 'Connection': 'keep-alive'}

    def __init__(self, headers=HEADERS):
        self.headers = headers
        try:
            self.conn = urllib3.HTTPConnectionPool('api.thesubdb.com', headers=self.headers)

        except Exception as e:
            print(e.args)
        
    def download(self, url, filename):
        try:
            response = self.conn.request("GET", url[url.rfind('/'):]) # for urllib3
            if response.status == 404:
                print("Couldn't find anything for " + filename[:-4])
            else:
                with open(filename, 'wb') as fout:

                    print("Found subtitles for " + filename[:-4])
                    fout.write(response.data)
        except Exception as e:
            print(e.args)
