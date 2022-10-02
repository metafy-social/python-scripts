from moviepy.editor import VideoFileClip
# import moviepy , videofileclip
import VideoFileClip

# replace "my-life.mp4" with your file name
videoClip = VideoFileClip("my-life.mp4")

# write whatever name you want for you gif file
videoClip.write_gif("my-life.gif")
