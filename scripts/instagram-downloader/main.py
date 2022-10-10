import urllib.request
import requests
import json
import re
import sys


def downloadVideo(postId):
    is_multiple_post = False
    videos = []
    url = requests.get("https://instagram.com/p/" + str(postId))
    if url.status_code == 404:
        print("Specified post not found")
        sys.exit()
    json_data = json.loads(re.findall(r"window._sharedData\s=\s(\{.*\});</script>", url.text)[0])
    data = json_data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]
    if "edge_sidecar_to_children" in data.keys():
        is_multiple_post = True
    isVideo = data["is_video"]
    if not isVideo and not is_multiple_post:
        print("Video not found!")
        sys.exit()
    if isVideo:
        videos.append(data["video_url"])
    if is_multiple_post:
        for post in data["edge_sidecar_to_children"]["edges"]:
            if post["node"]["is_video"]:
                videos.append(post["node"]["video_url"])
    print("Found " + str(len(videos)) + " videos")
    for number, video in zip(list(range(len(videos))), videos):
        print("Downloading video " + str(number + 1))
        urllib.request.urlretrieve(video, (postId + "_" + str(number + 1) + ".mp4"))


if len(sys.argv) == 1:
    print("Please enter the video ID")
else:
    downloadVideo(sys.argv[1])