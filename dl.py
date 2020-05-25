from aiogram.types import InputFile
import pafy
import os

PREF = '[YT Downloader]'
EX = 'm4a'

class Audio:
    def __init__(self, url):
        self._audio = pafy.new(url).getbestaudio(preftype=EX)
        self._title = self._audio.title
        self._caption = '@yt_audio_dl_bot'
        self._performer = PREF
        self._filename = (f'{self._title}.{EX}').replace('?', '').replace('\\', '').replace('/', '').replace('|', '')
        self._audio.download(filepath=os.path.join('temp_audios', self._filename))
        self._tg_file = InputFile(os.path.join('temp_audios', self._filename))

    def get_audio(self):
        return self._tg_file

    def get_title(self):
        return self._title

    def get_performer(self):
        return self._performer

    def get_caption(self):
        return self._caption

    def delete_audio(self):
        os.remove(os.path.join('temp_audios', self._filename))

class SizeError(Exception):
    pass