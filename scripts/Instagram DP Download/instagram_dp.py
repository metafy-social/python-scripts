# pip install instaloader
import instaloader

il = instaloader.Instaloader()
username = input("Enter username: ")
il.download_profile(username , profile_pic_only=True)
print(f"{username}'s DP is Downloaded!!")