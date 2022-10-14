import os
import shutil
from sys import platform
from threading import Thread

organise_folder = download_path = None

category = {"Audios": [".aif", ".cda", ".mid.mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl", ".midi"],
            "Compressed": [".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar", ".z", ".zip", ".gz"],
            "Documents": [".bin", ".dmg", ".iso", ".toast", ".vcd", ".csv", ".dat", ".db", ".log", ".mdb", ".sav",
                          ".sql", ".tar", ".xml", ".dbf", ".email", ".eml", ".emlx", ".msg", ".oft", ".ost", ".pst",
                          ".vcf", ".asp", ".cer", ".cfm", ".cgi", ".css", ".htm", ".js", ".jsp", ".part", ".php", ".py",
                          ".rss", ".xhtml", ".fnt", ".fon", ".otf", ".ttf", ".doc", ".odt", ".pdf", ".rtf", ".tex",
                          ".txt", ".wpd", ".key", ".odp", ".pps", ".ppt", ".pptx", ".c", ".cgi", ".class", ".cpp",
                          ".cs", ".h", ".java", ".php", ".py", ".sh", ".swift", ".vb", ".ods", ".xls", ".xlsm", ".xlsx",
                          ".docx", ".aspx", ".html"],
            "Images": [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".png", ".ps", ".psd", ".svg", ".tif", ".jpg", ".tiff"],
            "Videos": [".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg.rm", ".swf",
                       ".vob", ".wmv", ".mpeg", ".webm"],
            "Setups": [".apk", ".bat", ".bin", ".cgi", ".com", ".exe", ".gadget", ".jar", ".msi", ".py", ".wsf"],
            "Systemfiles": [".bak", ".cab", ".cfg", ".cpl", ".cur", ".dll", ".dmp", ".drv", ".icns", ".ico", ".ini",
                            ".lnk", ".msi",
                            ".sys", ".tmp"]}


def movers(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    try:
        shutil.move(source, destination)
    except OSError as error:
        print(str(source) + " <= File is open. Error => ", error)


def our_cat_dir(main_path, filepath):
    for cat in category:
        if filepath == os.path.join(main_path, cat):
            return True
    return False


def our_ext_dir(main_path, filepath):
    for cat in category:
        for ext in category[cat]:
            if filepath == os.path.join(main_path, ext):
                return True
    return False


def org_by_cat(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            if not our_cat_dir(path, file_path):
                Thread(target=org_by_cat, args=[file_path]).start()
                continue
        else:
            file_name, file_extension = os.path.splitext(file_path)
            for cat in category:
                cat_folder = os.path.join(path, cat)
                if file_extension.lower() in category[cat]:
                    movers(file_path, cat_folder)


def org_by_ext(path):
    for file in os.listdir(path):
        if os.path.isdir(file):
            if not our_ext_dir(path, file):
                Thread(target=org_by_ext, args=[file]).start()
                continue
        else:
            file_path = os.path.join(path, file)
            file_name, file_extension = os.path.splitext(file_path)
            for cat in category:
                if file_extension.lower() in category[cat]:
                    ext_folder = os.path.join(path, file_extension)
                    movers(file_path, ext_folder)


def main():
    global organise_folder, download_path
    if platform == "linux" or platform == "linux2":
        download_path = "/home/" + os.environ.get('USERNAME') + "/Downloads"
    elif platform == "win32":
        download_path = "C:\\Users\\" + os.environ.get('USERNAME') + "\\Downloads"
    while True:
        print("Press Q to exit anytime.")
        path = input('''\tOrganise Custom Directory? Enter Path (default : Downloads)\n>>>''')
        if path == "q":
            break
        elif path == "":
            organise_folder = download_path
        else:
            organise_folder = path
        if not os.path.exists(organise_folder):
            print("\nInvalid Path.")
            continue
        else:
            if os.path.isdir(organise_folder):
                break
            else:
                print("\nEntered Path not a directory.")
                continue
    while True:
        organise_type = input("\nIn what way do you want to organize.\n\t"
                              + "1) Organize files by category.\n\t"
                              + "2) Organize files by extension.\n>>>")
        if organise_type == "q":
            break
        elif organise_type == "1":
            print("Working")
            org_by_cat(organise_folder)
            print("Done")
            break
        elif organise_type == "2":
            print("Working")
            org_by_ext(organise_folder)
            print("Done")
            break


if __name__ == "__main__":
    main()
