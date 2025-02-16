# File-Organizer-Script

## Description:

This script automatically organizes files in the `Documents` directory (or another specified directory) 
by moving them into categorized folders based on their file extensions. It helps keep your workspace 
clean and makes file management more efficient.

## Features:

- Moves files based on predefined extensions.
- Categorizes files into folders such as `Images`, `Videos`, `Documents`, `Presentation`, and `Zips`.
- Prevents clutter in your `Documents` folder by automatically sorting new files.
- Exception handling for errors when moving files.

## Prerequisites:

Python 3.x installed on your system.

## Installation:

1. Download or copy the script to your local machine.
2. Ensure that the necessary folders (`Images`, `Videos`, `Documents`, `Presentation`, `Zips`) exist in your `Documents` directory. The script does not create them automatically.

## Usage:

1. Run the script using Python:

```shell
python file_organizer.py
```

2. The script will scan the `Documents` directory (or the specified directory) and move files with known extensions into their respective folders.
3. If a file has an extension not listed in the script, it will be left in place.

## File Extensions and Folders:

The script currently supports the following extensions and moves them into corresponding folders:

| Extension                | Folder       |
| ------------------------ | ------------ |
| .png, .jpg, .jpeg, .HEIC | Images       |
| .mp4, .MOV               | Videos       |
| .pdf, .docx              | Documents    |
| .pptx                    | Presentation |
| .zip                     | Zips         |

You can modify the `extensions` dictionary in the script to include additional file types or change the destination folders.

## Compatibility:

- **MacOS/Linux**: The script should work as expected by default.
- **Windows**: The script attempts to use `USERPROFILE` to determine the `Documents` folder, but I am **not 100% sure if it works correctly on Windows**. If you encounter issues, try manually setting the `directory` variable.

## Troubleshooting:

- Ensure the folders exist in the `Documents` directory before running the script.
- If a file fails to move, the script will print an error message (e.g., if a file with the same name already exists in the destination folder).
- You can modify the `directory` variable if you want to organize files in a different location.

## Future Improvements:

- Automatically create missing destination folders.
- Add support for more file extensions.
- Improve Windows compatibility.

## License:

This script is provided as-is with no guarantees. Feel free to modify and improve it as needed.
