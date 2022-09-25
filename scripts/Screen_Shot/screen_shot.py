import pyautogui
from time import sleep

def screenshot_fun():
	print("Screenshot program  runs on console\nchange the sleep time if you can the screenshot captured the terminal also")
	sleepTimer = 2
	print(f"You've {sleepTimer} to minimize the terminal window")
	sleep(2)
	print("Captured the screen now")
	screenshot_img = pyautogui.screenshot()
	screenshot_img.save("screen.png")

if __name__ == '__main__':
	screenshot_fun()
