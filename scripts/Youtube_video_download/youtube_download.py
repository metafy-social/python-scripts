from pytube import YouTube

link = input("Enter URL of YouTube video: ")
youtube = YouTube(link)

videos = youtube.streams.all()
videos_list = list(enumerate(videos))

for i in videos_list:
    print(i)

strm = int(input("Enter index number: "))
videos[strm].download()
print("YouTube video Downloaded successfully!!")
