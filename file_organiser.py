import os # Needed to get paths
import shutil # Needed to move files


# Key: extension, Value: folder. You can add every extension that you want/
# NOTE: the folder must be created in the directory of choice for the code to work!

EXTENSIONS = {
    # Images
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".heic": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".tiff": "Images",
    ".webp": "Images",
    ".svg": "Images",

    # Videos
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",
    ".m4v": "Videos",

    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".rtf": "Documents",
    ".odt": "Documents",
    ".md": "Documents",

    # Presentations
    ".ppt": "Presentation",
    ".pptx": "Presentation",
    ".key": "Presentation",
    ".odp": "Presentation",

    # Spreadsheets
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".ods": "Spreadsheets",

    # Archives / Zips
    ".zip": "Zips",
    ".rar": "Zips",
    ".7z": "Zips",
    ".tar": "Zips",
    ".gz": "Zips",
    ".bz2": "Zips",

    # Audio
    ".m4a": "Audio",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",
    ".flac": "Audio",
    ".ogg": "Audio",

    # Code
    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".json": "Code",
    ".xml": "Code",
    ".yml": "Code",
    ".yaml": "Code",

    # Executables
    ".exe": "Executables",
    ".msi": "Executables",
    ".app": "Executables",
    ".dmg": "Executables",
}


def move_file(item_path, path_to_directory, extension):
    """
    Moves the file to the specified directory and prints success message.
    """
    shutil.move(item_path, path_to_directory)

    print(f"{os.path.split(item_path)[1]} moved successfully to {EXTENSIONS[extension]}!")

def file_exists_options():
    """
    Prints out the available options in case there is a duplicate file in the dir.
    """
    divider = "-" * 30

    print(divider)

    print("1) Ignore file")
    print("2) Replace existing file")

    print(divider)


def main():
    directory = ""

    if os.name == "nt":  # Windows (not sure)
        directory = os.path.join(os.getenv("USERPROFILE"),
                                 "Documents")  # Change 'Documents' if you want to organise your files in a different directory
    else:  # macOs/Linux
        directory = os.path.expanduser(
            "~/Documents")  # Change 'Documents' if you want to organise your files in a different directory

    for item in os.listdir(directory):  # Iterates through all folders and files in the directory
        item_path = os.path.join(directory, item)  # path to folder or path

        if os.path.isfile(item_path):  # If it is a file then it must be put in a folder(if the extension is added to extensions *see line 7)
            f, ex = os.path.splitext(item)  # file and extension

            if ex in EXTENSIONS.keys():  # Checks(by key) if the extension is in 'extensions' dictionary.
                path_to_directory = os.path.join(directory, EXTENSIONS[ex])  # Gets the path to the folder that the file will be putted in.

                try:
                    move_file(item_path, path_to_directory, ex)
                except shutil.Error as e:  # If there is an error with moving the file, it will be caught
                    if "already exists" in e.args[0]:
                        print(e)

                        file_exists_options()
                        choice = input("Your choice: ")

                        choice = int(choice.strip())

                        if choice == 2:
                            # Gets the path of the already existing file
                            path_to_existing_file = os.path.join(path_to_directory, f"{f}{ex}")
                            os.remove(path_to_existing_file)
                            move_file(item_path, path_to_directory, ex)
                        elif choice != 1 and choice != 2:
                            print("Invalid choice. File will be ignored.")


if __name__ == "__main__":
    main()
