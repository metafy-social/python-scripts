# Automate Win, Mac and Linux
# pip install PyAutoGUI
import pyautogui as py
# Mouse Movements
py.moveTo(100, 100)
py.moveTo(200, 200, duration=1)
py.click(100, 100)
py.doubleClick(200, 200)
# Keyboard Inputs
py.write('Hello World!', interval=0.25)
py.press('enter')
py.hotkey('ctrl', 'c')
py.keyDown('shift')
py.keyUp('shift')
# Screen Automation
img = py.screenshot('screenshot.jpg')
img.save('screenshot.jpg')
loc = py.locationsOnScreen('icon.jpg')
print(loc)