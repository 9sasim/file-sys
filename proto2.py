import os
from simple_term_menu import TerminalMenu

class FileSystemManager:
    def create_file(self):
        file_name = input("Enter the filename or file path to save in different directory (e.g: /home/user-directory/file_name): ")
        if os.path.exists(file_name):
            print("File already exists.")
        else:
            with open(file_name, 'w') as f:
                print(f"{file_name} created successfully.")


options = ["[1] Create File","[2] Read File","[3] Write to File","[4] Create and write to file","[5] Delete File","[6] Create Directory","[7] Create Directory and create a file","[8] Create a Directory and a file and write to file","[9] Lists the files in a Directory", "[10] Search Files in Directory","[11] Delete Directory","[12] Change Permission", "[13] Exit"]

mainMenu = TerminalMenu(options, title = " Welcome")

quitting = False

while quitting == False:
    try:
        optionsIndex =mainMenu.show()
        optionsChoice = options[optionsIndex]

        if (optionsChoice == "[13] Exit"):
            qutting = True
        elif (optionsChoice == "[1] Create File"):
            self.create_file()
        else:
            print(optionsChoice)
            break
    except KeyboardInterrupt:
        a = input("\nDo you want to terminate (Y/N): ")
        if a.lower()== "y":
            print("Terminating....")
            break
        else:
            continue