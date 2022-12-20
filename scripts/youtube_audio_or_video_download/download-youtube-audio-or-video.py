from pytube import YouTube
import os

def audio_only():
    print('------------------------------')
    print('Hey, you are about to download the audio of the YouTube video of your choice')
    print("Don't know why you need that though, but enjoyyyy.")
    print('------------------------------\n')

    video_url = str(input("Enter the YouTube video URL: "))
    yt = YouTube(video_url)

    #path to save to
    path = os.getcwd() + '\\'

    #video title
    title = yt.title

    #download audio
    audio = yt.streams.filter(only_audio=True).first()
    audio_file = audio.download(output_path=path)
    
    #save file
    base, extension = os.path.splitext(audio_file)
    new_audio_file = base + '.mp3'
    os.rename(audio_file, new_audio_file)

    print(title + " has been successfully downloaded.")

def video():
    print('------------------------------')
    print('Hey, you are about to download the YouTube video of your choice')
    print("Enjoyyyy.")
    print('------------------------------\n')

    video_url = str(input("Enter the YouTube video URL: "))
    yt = YouTube(video_url)

    #path to save to
    path = os.getcwd() + '\\'

    #video title
    title = yt.title

    #download video
    video = yt.streams.filter(res='1080p').first()
    video_file = video.download(output_path=path)
    
    #save file
    base, extension = os.path.splitext(video_file)
    new_audio_file = base + '.mp4'
    os.rename(video_file, new_audio_file)

    print(title + " has been successfully downloaded.")

def main():
    download = str(input('Video or Audio_only? (V|A): '))

    if download == "V":
        video()
    else: 
        audio_only()    

if __name__ == '__main__':
    main()