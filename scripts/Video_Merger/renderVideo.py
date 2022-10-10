from moviepy.editor import VideoFileClip,concatenate_videoclips 
from listvideos import videoslist,pathOfVideo
import os


def renderFinalVideo():
  videoNames=[VideoFileClip(os.path.join(pathOfVideo, video)) for video in videoslist]
  final_video = concatenate_videoclips(videoNames,method='compose')
  filePath= input("Enter location to save file:-")
  filePathExists= os.path.exists(filePath)
  if filePathExists:
    fileName= input("Enter file name;-")

    if fileName.endswith(".mp4"):
      final_video.write_videofile(os.path.join(filePath,fileName))
    else:
      print("Sorry the extension must be .mp4")

  else:
    print(f"Sorry Error Occured!!!Make sure this path exists:- {filePath}")