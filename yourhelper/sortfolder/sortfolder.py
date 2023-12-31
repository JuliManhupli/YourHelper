from .classes import SortFolder, NormalizeName, UnpackArchive
import os
from yourhelper.styles import stylize


def sort_folder_run() -> None:
    """Prompt user for folder path and run sorting on it"""

    while True:

        print(
            'Enter the path to the folder in which you want to organize or enter "Back" to return to the previous menu:')
        path = input('>>> ').strip("\"\'")

        if path.lower() in ('back', "exit", "close", 'quit', 'q', '0'):
            break

        if not os.path.exists(path):
            print(stylize('Folder ', 'red') + path + stylize(' does not exist.', 'red'))
            continue

        sort = SortFolder(path)
        print(sort.run())
        break


def normalize_name() -> None:
    """Prompt user for file/folder path and normalize its name"""

    while True:

        print(
            'Enter the path of the file or folder for which you want to normalize the name or enter "Back" to return to the previous menu:')
        path = input('>>> ').strip("\"\'")

        if path.lower() in ('back', "exit", "close", 'quit', 'q', '0'):
            break

        if not os.path.exists(path):
            print(path + stylize(' does not exist.', 'red'))
            continue

        normalize = NormalizeName()
        print(normalize.rename(path))
        break

def unpack_archive() -> None:
    """Prompt user for archive path and unpack it"""

    while True:

        print('Enter the path to the archive you want to unpack or enter "Back" to return to the previous menu:')
        path = input('>>> ').strip("\"\'")

        if path.lower() in ('back', "exit", "close", 'quit', 'q', '0'):
            break

        if not os.path.exists(path):
            print(path + stylize(' does not exist.', 'red'))
            continue

        unpac = UnpackArchive(path)
        print(unpac.extract())
        break


handler = {
    '1': sort_folder_run,
    '2': normalize_name,
    '3': unpack_archive,
}


def start() -> None:
    """Display welcome and initial command prompt loop"""

    print(stylize("\nWelcome to the Sortfolder!", 'white', 'bold'))

    while True:
        print(stylize('Select a command:', '', 'bold'))
        print('1 - Sort folder')
        print('2 - File or folder name normalization')
        print('3 - Unpack an archive')
        print('0 - Return to the main menu')
        command = input("Enter a command: ").strip()
        if command == '0':
            print()
            break
        elif command in handler:
            handler[command]()
        else:
            print(stylize("The command is incorrect\n", 'red'))
