import pafy

PREF = '[YT Downloader]'
EX = 'm4a'


#
# try:
#     video = pafy.new(input('YT link to download: '))
#     # a_streams = video.audiostreams
#     # for a in reversed(a_streams):
#     #     print(a.bitrate, a.extension, a.get_filesize())
#
#     a_streams = video.audiostreams
#     for stream in reversed(a_streams):
#         if stream.extension == 'm4a':
#             if stream.get_filesize()/1000000 <= 50:
#                 print(stream.title)
#                 stream.download()
#             else:
#                 print('audio is larger then 50 mb!')
# except ValueError:
#     print('invalid link!')

class Audio:
    def __init__(self, url):
        self._audio = pafy.new(url).getbestaudio(preftype=EX)
        print(self._audio.title)
        self._title = f'{PREF} {self._audio.title}'
        self._filename = (self._title + '.' + EX).replace('?', '')
        self._audio.download(filepath='temp_audios/' + self._filename)
        # self.tg_file = InputFile('temp_audios/' + self._filename)

audio = Audio('https://www.youtube.com/watch?v=jOqmkeHzedM')

# aud = pafy.new('https://www.youtube.com/watch?v=jOqmkeHzedM')
# audiostreams = aud.audiostreams
# for a in audiostreams:
#     print(a.bitrate, a.extension, a.get_filesize())