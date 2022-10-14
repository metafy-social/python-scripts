import time
import os
import pickle
import tkinter as tk
from tkinter import Label, filedialog
from tkinter import PhotoImage
from pygame import mixer
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
from tkinter import messagebox


class Player(tk.Frame):
    def __init__(self, song_path, master=None):
        super().__init__(master)
        self.master = master
        self.song_path = song_path
        self.pack()
        mixer.init()

        if os.path.exists('songs.pickle'):
            with open('songs.pickle', 'rb') as f:
                self.playlist = pickle.load(f)
        else:
            self.playlist = []

        self.current = 0
        self.paused = True
        self.played = False
        self.song_length = 0

        self.page_layouts()
        self.track_config()
        self.control_widgets()
        self.song_list()
        self.retrieve_songs2()

    def page_layouts(self):
        self.track = tk.LabelFrame(self, text='Song Track',
                                   font=("times new roman", 15, "bold"),
                                   bg="black", fg="white", bd=5, relief=tk.GROOVE)
        self.track.config(width=400, height=300)
        self.track.grid(row=0, column=0, padx=1)

        self.tracklist = tk.LabelFrame(self, text=f'PlayList - {str(len(self.playlist))}',
                                       font=("times new roman", 12, "bold"),
                                       bg="black", fg="white", bd=5, relief=tk.GROOVE)
        self.tracklist.config(width=190, height=200)
        self.tracklist.grid(row=0, column=1, pady=1)

        self.controls = tk.LabelFrame(self,
                                      font=("times new roman", 15, "bold"),
                                      bg="black", fg="white", bd=2, relief=tk.GROOVE)
        self.controls.config(width=410, height=80)
        self.controls.grid(row=2, column=0, pady=1, padx=1)

        self.music_slider = tk.LabelFrame(self,
                                          font=("times new roman", 15, "bold"),
                                          bg="black", fg="white", bd=5, relief=tk.GROOVE)
        self.music_slider.config(width=410, height=80)
        self.music_slider.grid(row=3, column=0, pady=1, padx=1)

        self.func = tk.LabelFrame(self,
                                  font=("times new roman", 12, "bold"),
                                  bg="black", fg="white", bd=5, relief=tk.GROOVE)
        self.func.config(width=250, height=210)
        self.func.grid(row=3, column=1)

        self.promo = tk.LabelFrame(self,
                                   bg="black", fg="white", bd=5, relief=tk.GROOVE)
        self.promo.config(width=50, height=50)
        self.promo.grid(row=2, column=1)

    def track_config(self):
        self.views = tk.Label(self.track, image=img)
        self.views.configure(width=400, height=240)
        self.views.grid(row=0, column=0)

        self.musictrack = tk.Label(self.track, font=("times new roman", 16, "bold"),
                                   bg="white", fg="dark blue")
        self.musictrack['text'] = 'MP3 Player'
        self.musictrack.config(width=30, height=1)
        self.musictrack.grid(row=1, column=0, padx=10)

    def control_widgets(self):
        self.loading = tk.Button(
            self.controls, bg='green', fg='white', font=10)
        self.loading['text'] = 'Load Songs'
        self.loading['command'] = self.retrieve_songs
        self.loading.grid(row=0, column=0, padx=10)

        self.prev = tk.Button(self.controls, image=prev)
        self.prev['command'] = self.prev_song
        self.prev.grid(row=0, column=1)

        self.pause = tk.Button(self.controls, image=pause)
        self.pause['command'] = self.pause_song
        self.pause.grid(row=0, column=2)

        self.next = tk.Button(self.controls, image=next_)
        self.next['command'] = self.next_song
        self.next.grid(row=0, column=3)

        self.volume = tk.DoubleVar(self)
        self.slider = tk.Scale(self.controls, from_=0,
                               to=10, orient=tk.HORIZONTAL)
        self.slider['variable'] = self.volume
        self.slider.set(5)
        mixer.music.set_volume(1)
        self.slider['command'] = self.change_volume
        self.slider.grid(row=0, column=4, padx=10, pady=4)

        self.mu_slider = ttk.Scale(self.music_slider, from_=0, to=100,
                                   orient=tk.HORIZONTAL, value=0, length=390)
        self.mu_slider.grid(pady=20, padx=10)

        self.status_bar = Label(self.music_slider, text="Time Elapsed: 0/0")
        self.status_bar.grid(pady=1)

        self.delet = tk.Button(self.func, text="Delete", bg='green', fg='white', font=15)
        self.delet['command'] = self.delete_songs
        self.delet.grid(row=0, column=1, padx=39, pady=29)

        self.prom = tk.Label(self.promo, text="artgoblin's work", font=("times new roman", 10, "bold", "italic"),
                             bg="grey", fg="black")
        self.prom.grid(row=0, column=2, padx=20, pady=12)

    def song_list(self):
        self.scrollbar = tk.Scrollbar(self.tracklist, orient=tk.VERTICAL)
        self.scrollbar.grid(row=0, column=1, rowspan=5, sticky='ns')

        self.list = tk.Listbox(self.tracklist, selectmode=tk.SINGLE,
                               yscrollcommand=self.scrollbar.set, selectbackground='sky blue')
        self.enum_songs()
        self.list.config(height=17)
        self.list.bind('<Double-1>', self.play_song)

        self.scrollbar.config(command=self.list.yview)
        self.list.grid(row=0, column=0, rowspan=5)

    def retrieve_songs2(self):
        self.songlist2 = []
        os.chdir(self.song_path)

        for files in os.listdir(self.song_path):
            try:
                if files.endswith(".mp3"):

                    self.songlist2.append(files)
                elif files.endswith(".wav"):

                    self.songlist2.append(files)
                elif files.endswith(".mpeg"):

                    self.songlist2.append(files)
            except:
                pass

        with open('songs2.pickle', 'wb') as f:
            pickle.dump(self.songlist2, f)
        self.playlist = self.songlist2
        self.tracklist['text'] = f'PlayList - {str(len(self.playlist))}'
        self.list.delete(0, tk.END)

        self.enum_songs()

    def retrieve_songs(self):
        self.songlist = []

        directory = filedialog.askdirectory()
        for root_, dirs, files in os.walk(directory):
            for file in files:
                if os.path.splitext(file)[1] == '.mp3':
                    path = (root_ + '/' + file).replace('\\', '/')
                    self.songlist.append(path)
                elif os.path.splitext(file)[1] == '.mpeg':
                    path = (root_ + '/' + file).replace('\\', '/')
                    self.songlist.append(path)
                elif os.path.splitext(file)[1] == '.wav':
                    path = (root_ + '/' + file).replace('\\', '/')
                    self.songlist.append(path)

        with open('songs.pickle', 'wb') as f:
            pickle.dump(self.songlist, f)
        self.playlist = self.songlist
        self.tracklist['text'] = f'PlayList - {str(len(self.playlist))}'
        self.list.delete(0, tk.END)
        self.enum_songs()

    def enum_songs(self):
        for index, song in enumerate(self.playlist):
            self.list.insert(index, os.path.basename(song))

    def play_song(self, event=None):
        if event is not None:
            self.current = self.list.curselection()[0]
            for i in range(len(self.playlist)):
                self.list.itemconfigure(i, bg="white")

        print(self.playlist[self.current])
        mixer.music.load(self.playlist[self.current])
        self.m = mixer.music.load(self.playlist[self.current])
        self.musictrack['anchor'] = 'w'
        self.musictrack['text'] = os.path.basename(self.playlist[self.current])

        self.pause['image'] = play
        self.paused = False
        self.played = True
        self.list.activate(self.current)
        self.list.itemconfigure(self.current, bg='sky blue')

        mixer.music.play()
        self.update_progress()

    def update_progress(self):
        song_mut = MP3(self.playlist[self.current])
        self.song_length = song_mut.info.length
        slider_position = int(self.song_length)
        self.mu_slider.config(to=slider_position)
        pos_ms = mixer.music.get_pos() / 1000
        self.mu_slider.config(value=pos_ms)
        clock = time.strftime('%M:%S', time.gmtime(self.song_length))
        clock2 = time.strftime('%M:%S', time.gmtime(pos_ms))
        self.status_bar.config(text=f'Time Elapsed: {clock2} /  {clock}  ')
        self.after(1000, self.update_progress)

    def pause_song(self):
        if not self.paused:
            self.paused = True
            mixer.music.pause()
            self.pause['image'] = pause
        else:
            if self.played == False:
                self.play_song()
            self.paused = False
            mixer.music.unpause()
            self.pause['image'] = play

    def prev_song(self):
        if self.current > 0:
            self.current -= 1
        else:
            self.current = 0
        self.list.itemconfigure(self.current + 1, bg='white')
        self.play_song()

    def next_song(self):
        if self.current < len(self.playlist) - 1:
            self.current += 1
        else:
            self.current = 0
        self.list.itemconfigure(self.current - 1, bg='white')
        self.play_song()

    def change_volume(self, event=None):
        self.v = self.volume.get()
        mixer.music.set_volume(self.v / 10)

    def delete_songs(self, event=None):
        items = map(int, self.list.curselection())
        for item in items:
            self.list.delete(item)
            self.playlist.pop(item)
        self.tracklist['text'] = 'Total Songs: ' + str(len( self.playlist))
        
    
     


def run(song_path):
    global img, prev, play, next_, pause
    root = tk.Tk()
    root.title('MP3 Player')
    root.geometry("572x458")

    def on_closing():

        if messagebox.askokcancel("Quit", "Do you want to quit?"):

            mixer.music.stop()
            root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_closing)

    os.path.join(os.path.curdir, 'file.name')

    img = PhotoImage(file=os.path.join(os.path.curdir, 'images/image2.gif'))
    next_ = PhotoImage(file=os.path.join(os.path.curdir, 'images/next.gif'))
    prev = PhotoImage(file=os.path.join(os.path.curdir, 'images/previous.gif'))
    play = PhotoImage(file=os.path.join(os.path.curdir, 'images/play.gif'))
    pause = PhotoImage(file=os.path.join(os.path.curdir, 'images/pause.gif'))
  
    app = Player(song_path, master=root)
    app.mainloop()