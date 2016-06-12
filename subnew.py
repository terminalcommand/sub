from moviesearch import MovieSearch
from subdb import SubDB
from downloader import Downloader

import concurrent.futures

moviesearcher = MovieSearch()
subsearcher = SubDB()
# need to implement addict7ed support
subdownloader = Downloader()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    for i in moviesearcher.return_files():
        link = subsearcher.process(i)
        print(i)
        print(link)
#        subdownloader.download(link, moviesearcher.get_name(i)+'.srt')
        executor.submit(subdownloader.download, link, moviesearcher.get_name(i)+'.srt')
