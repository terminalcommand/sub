import os
import hashlib

class SubDB:
    def init(self):
        pass
    def get_hash(self, name):
        readsize = 64 * 1024
        with open(name, 'rb') as f:
            readsize = readsize
            size = os.path.getsize(name)
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)
        return hashlib.md5(data).hexdigest()
    def gen_dl_link(self, hsh):
        return 'http://api.thesubdb.com/?action=download&hash=' + hsh + '&language=en'
    def process(self, name):
        return self.gen_dl_link(self.get_hash(name))
