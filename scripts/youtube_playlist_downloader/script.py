from tkinter import *
from pyyoutube import Api
from pytube import YouTube
from threading import Thread
from tkinter import messagebox


def threading():
	t1 = Thread(target=download_videos)
	t1.start()


def download_videos():
	api = Api(api_key='Enter API Key')

	if "youtube" in playlistId.get():
		playlist_id = playlistId.get()[len(
			"https://www.youtube.com/playlist?list="):]
	else:
		playlist_id = playlistId.get()

	playlist_item_by_id = api.get_playlist_items(
		playlist_id=playlist_id, count=None, return_json=True)

	for index, videoid in enumerate(playlist_item_by_id['items']):

		link = f"https://www.youtube.com/watch?v={videoid['contentDetails']['videoId']}"

		yt_obj = YouTube(link)

		filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

		filters.get_highest_resolution().download()

		print(f"Downloaded:- {link}")

	messagebox.showinfo("Success", "Video Successfully downloaded")


root = Tk()
root.geometry('400x200')

Label(root, text="Youtube Playlist Downloader",
	font="italic 15 bold").pack(pady=10)
Label(root, text="Enter Playlist URL:-", font="italic 10").pack()


playlistId = Entry(root, width=60)
playlistId.pack(pady=5)

download_start = Button(root, text="Download Start", command=threading)
download_start.pack(pady=10)

root.mainloop()
