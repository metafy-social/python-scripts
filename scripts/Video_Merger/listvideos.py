
#this script returns the list of videos (.mp4) from the path you choose. 
import os
pathOfVideo=input("Enter the full path where videos are located.")

def array_Of_Videos():
  fileExists= os.path.exists(pathOfVideo) #returns a boolen
 
  if fileExists:
    dirList= sorted(os.listdir(pathOfVideo)) #returns list of files inside the path
    return [files for files in dirList if files.endswith(".mp4") ]
  
  else:
      print(f"No such path as {pathOfVideo}")

videoslist= array_Of_Videos()
print(f'If the sequence of the videos doesn\'t look like Following. You can press Control + C to kill the program.\n{videoslist}')
