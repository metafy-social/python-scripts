"""Bulk renamer in python"""
import os

def bulk_renamer(path, extension, files_name):
    """Function to bulk rename files"""
    files_count = 1
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == f".{extension}":
            os.rename(f"{path}{file}",
                      f"{path}{files_name}{files_count}.{extension}")
            files_count += 1


if __name__ == '__main__':
    files_path = input("Enter the directory path: ")
    files_extension = input("Enter the file extension to rename: ").lower()
    renamed_name = input("What you want to name your files?: ")
    bulk_renamer(files_path, files_extension, renamed_name)
    print("Done! \nCheck your files...")
