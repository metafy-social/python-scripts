import os
import sys
import platform
import subprocess

# Seeing if the file exists
if os.path.exists(sys.argv[1]):
    # Open Only if the file exists on the computer
    f = open(sys.argv[1], "r")
    # Storing the Content of the file in the f_contents variable
    f_contents = f.read()
    # closing the opened file
    f.close()
else:
  # If the file Doesn't Exists
    print("File Not found : copy2clip <file_name>")
    exit(1)
# Storing the current OS version
whatos = platform.system()
# If Darwin or Ubuntu
if whatos == "Darwin":
    subprocess.run("pbcopy", universal_newlines=True, input=f_contents)
    print("success: copied to clipboard")
# If Windows
elif whatos == "Windows":
    subprocess.run("clip", universal_newlines=True, input=f_contents)
    print("success: copied to clipboard")
else:
    print("failed: clipboard not supported")
