import os

class MovieSearch:
    EXTS = ['.mp4', '.avi', '.mkv', '.mov']
    def __init__(self, path=None):
        get_ext = lambda x: os.path.splitext(x)[1] # just a fancy renaming for os.path.splittext
        get_name = lambda x: os.path.splitext(x)[0]
        self.get_name = get_name # for uses outside the function
        os.chdir(path) if path else print("No path specified. Searching for movies in the current directory!")
        self.files = [i for i in os.listdir() if get_ext(i) in MovieSearch.EXTS]
        self.subs = [get_name(i) for i in os.listdir() if get_ext(i) in ['.srt']] # subs don't have the extension on them
        print("Ignoring the files that have subtitles...")
        self.files = [i for i in self.files if get_name(i) not in self.subs]
    def list_files(self):
        print("Video files to be subtitled: ")
        print(*self.files, sep='\n')
    def return_files(self):
        return self.files

if __name__ == '__main__':
    # for testing purposes
    a = MovieSearch()
    a.list_files()

