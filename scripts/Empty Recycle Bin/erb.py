import winshell
try:
    cmd = winshell.recycle_bin().empty(confirm=False, sound=True)
    print("Recycle bin is emptied now !")
except cmd:
    print("Recycle bin was already empty !")
