from moviesearch import MovieSearch
from subdb import SubDB
from downloader import Downloader

moviesearcher = MovieSearch()
subsearcher = SubDB()
# need to implement addict7ed support
subdownloader = Downloader()
for i in moviesearcher.return_files():
    link = subsearcher.process(i)
    print(i)
    print(link)
    subdownloader.download(link, moviesearcher.get_name(i)+'.srt')
