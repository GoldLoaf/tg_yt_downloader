from aiogram.types import InputFile
import pafy

def best_audio(streams):
    for stream in reversed(streams):
        if stream.extension == 'm4a':
            if stream.get_filesize()/1000000 <= 50:
                stream.download()
            else:
                raise 

class Audio:
    def __init__(self, url):

