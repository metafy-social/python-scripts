#!/usr/bin/python3
#CoDeD By AnAnT
import os, re, time, sys, platform
if os.name=='posix':
    clrval = 'clear'
else:
    clrval = 'cls'
def pattern1(label):
    """
    First introduction pattern for the program

    Args:
    label str: A string value is passed to be printed in the center
    """
    print('<-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+>')
    print(f'<====================={label}=====================>')
    print('<-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+>')
def pattern2(label):
    """
    Second introduction pattern for the program

    Args:
    label str: A string value is passed to be printed in the center
    """
    print('<_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*>')
    print(f'<====================={label}=====================>')
    print('<_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*>')
def patterndriver():
    """
    A driver function to syncronize the two print patterns. 
    """
    label = 'coded by anant'
    for i in range(3):
        os.system(clrval)
        label = label.lower()
        pattern1(label)
        time.sleep(0.50)
        os.system(clrval)
        label = label.upper()
        pattern2(label)
        time.sleep(0.50)
    print("BULK FILE RENAMER".center(58))
    print(f"\nOperating system-\n{sys.platform}\n{platform.release()}\n")
    print("Press ENTER to start program")
    sys.stdin.read(1)
def clearscr():
    """
    Clears the screen for further commands and prints the pattern.
    """
    os.system(clrval)
    print('<========================================================>')
    print('<=====================CoDeD By AnAnT=====================>')
    print('<========================================================>')
def change_path():
    """
    Changes the path to the desired folder.

    Returns:
    bool: Returns False if wrong path is provided, else returns True
    """ 
    try:
        clearscr()
        os.chdir(input('Enter the new directory-\n'))
    except FileNotFoundError:
        print('Wrong path given, try again.')
        return False
    return True
def check_file(newname):
    files = os.listdir()
    if newname not in files:
        return True
    else:
        return False

def bulk_rename(files):
    """
    Renames all files with a common name, appending numbers at the end.
    """
    commonstr = input('Enter the name for all files.\n')
    counter = 0
    newname = ''
    for file in files:
        extregex = re.compile(r'\..+$')
        extension = extregex.search(file)
        counter += 1
        try:
            newname = f'{commonstr}_{counter}{file[extension.start():extension.end()]}'
        except Exception as e:
            print(f'Error while renaming {file}\n{e}')
        os.rename(file, newname)
    print('All Files Are Renamed. Press ENTER to exit')
    sys.stdin.read(1)
    return 0
def single_rename(files):
    """
    Rename Files one by one, each file's name is displayed, new name is replaced.
    """
    for file in files:
        extregex = re.compile(r'\..+$')
        extension = extregex.search(file)
        print(f'Enter new name for {file}. Press ENTER to skip')
        filler = input()
        if filler.upper() == '':
            pass
        else:
            newname = f'{filler}{file[extension.start():extension.end()]}'
            if check_file(newname) == True:
                os.rename(file, newname)
            else:
                print('Name already taken, moving on')
                continue
        clearscr()
def ext_rename(files):
    """
    Renames files with a specific extension.

    Returns:
    int: Returns 0 after successful execution of program
    """
    flag = False
    extension = input('Enter the file type to be searched.\n')
    files = os.listdir()
    files.sort()
    specific_files = list()
    for file in files:
        if extension == file[-len(extension)::] and file[-len(extension)-1:-len(extension):]==".":
            specific_files.append(file)
            flag = True
    if flag == False:
        print("Extension Not Found")
        return 0
    clearscr()
    ext_method = input('Extension Found\nSelect the rename method\n-> One by One(O)\n-> Bulk(B)\n')
    if ext_method.upper() == "B":
        bulk_rename(specific_files)
    elif ext_method.upper() == "O":
        single_rename(specific_files)
if __name__=="__main__":
    """
    Driver function to execute other functions.
    """
    try:
        os.chdir(sys.argv[1])
    except:
        pass
    patterndriver()
    clearscr()
    directory = input(f'Current Directory- {os.getcwd()}\nWant to change?(Y/N)\n')
    if directory.upper() == 'Y':
        while (change_path()!=True):
            continue
        print(f'\nPath changed to {os.getcwd()}\n')
        sys.stdin.read(1)
        clearscr()
    print("Files in the directory are\n")
    print(*os.listdir(), sep='\n')
    # os.system('ls')
    print("\nFiles in this folder will be renamed")
    print("Select the rename method-\n")
    print("-> All at once (A)")
    print("-> One by one (O)")
    print("-> Rename by extension (E)\n")
    rename_method = input()
    clearscr()
    files = os.listdir()
    files.sort()
    if rename_method.upper() == "A":
        bulk_rename(files)
    elif rename_method.upper() == "E":
        ext_rename(files)
    else:
        single_rename(files)

#CoDeD By AnAnT

