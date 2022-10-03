import sys
from moviepy.editor import VideoFileClip

VideoFileClip(sys.argv[1]).audio.write_audiofile(sys.argv[2])