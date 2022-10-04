import moviepy.editor

path_video = input("Enter the path of video: ")
video = moviepy.editor.VideoFileClip(path_video)

audio = video.audio
path_audio = input("Enter the path of audio:")
audio.write_audiofile(path_audio)
