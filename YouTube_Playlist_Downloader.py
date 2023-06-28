from pytube import Playlist

py = Playlist("https://www.youtube.com/playlist?list=PL4x7Of-X4XhgNBVfFpd1N4cSU_X1x96gU")

print(f'Downloading : {py.title}')

for video in py.videos:
    video.streams.first().download()