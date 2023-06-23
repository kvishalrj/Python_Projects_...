from pytube import YouTube

link = "https://www.youtube.com/watch?v=Tl4bQBfOtbg"
youtube_1 = YouTube(link)

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)

# videos = youtube_1.streams.all() # All Format

videos = youtube_1.streams.filter(only_audio=True) # Only Audio Format

vid = list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input("Enter : "))
videos[strm].download()
print("Successfully Downloaded")