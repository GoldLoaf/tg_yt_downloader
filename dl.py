from aiogram.types import InputFile
import pafy

PREF = '[YT Downloader]'
EX = 'm4a'

class Audio:
    def __init__(self, url):
        self._audio = pafy.new(url).getbestaudio(preftype=EX)
        self._title = f'{PREF} {self._audio.title}'
        self._filename = self._title + '.' + EX
        self._audio.download(filepath='temp_audios/' + self._filename)
        self.tg_file = InputFile('temp_audios/' + self._filename)

    def get_audio(self):
        return self.tg_file

    def get_title(self):
        return self._title

class SizeError(Exception):
    pass

