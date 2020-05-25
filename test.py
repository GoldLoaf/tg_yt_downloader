import pafy

try:
    video = pafy.new(input('YT link to download: '))
    # a_streams = video.audiostreams
    # for a in reversed(a_streams):
    #     print(a.bitrate, a.extension, a.get_filesize())

    a_streams = video.audiostreams
    for stream in reversed(a_streams):
        if stream.extension == 'm4a':
            if stream.get_filesize()/1000000 <= 50:
                print(stream.title)
                stream.download()
            else:
                print('audio is larger then 50 mb!')
except ValueError:
    print('invalid link!')