import os # Needed to get paths
import shutil # Needed to move files


# Key: extension, Value: folder. You can add every extension that you want/
# NOTE: the folder must be created in the directory of choice for the code to work!
extensions = {
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".HEIC": "Images",
    ".mp4": "Videos",
    ".MOV": "Videos",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".pptx": "Presentation",
    ".zip": "Zips"
}

directory = ""

if os.name == "nt":  # Windows (not sure)
    directory = os.path.join(os.getenv("USERPROFILE"), "Documents") # Change 'Documents' if you want to organise your files in a different directory
else:  # macOs/Linux
    directory = os.path.expanduser("~/Documents") # Change 'Documents' if you want to organise your files in a different directory

for item in os.listdir(directory): # Iterates through all folders and files in the directory
    item_path = os.path.join(directory, item) # path to folder or path

    if os.path.isfile(item_path): # If it is a file then it must be put in a folder(if the extension is added to extensions *see line 7)
        f, ex = os.path.splitext(item) # file and extension

        if ex in extensions.keys(): # Checks(by key) if the extension is in 'extensions' dictionary.
            path_to_directory = os.path.join(directory, extensions[ex]) # Gets the path to the folder that the file will be putted in.

            try:
                shutil.move(item_path, path_to_directory) # If everything is successful, the file will be moved.
            except shutil.Error as e: # If there is an error with moving the file, it will be caught
                print(e) # Prints out the Exception
            else:
                print(f"{os.path.split(item_path)[1]} moved successfully to {extensions[ex]}!") # Message to let the user know that the file is moved
