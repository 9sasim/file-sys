import os
import subprocess
from simple_term_menu import Terminalmenu


word = r"""
   _,---.   .=-.-.             ,----.           ,-,--.                  ,-,--.  ,--.--------.    ,----.         ___   
  .-`.' ,  \ /==/_ / _.-.     ,-.--` , \        ,-.'-  _\ ,--.-.  .-,--.,-.'-  _\/==/,  -   , -\,-.--` , \ .-._ .'=.'\  
 /==/_  _.-'|==|, |.-,.'|    |==|-  _.-`       /==/_ ,_.'/==/- / /=/_ //==/_ ,_.'\==\.-.  - ,-./==|-  _.-`/==/ \|==|  | 
/==/-  '..-.|==|  |==|, |    |==|   `.-.       \==\  \   \==\, \/=/. / \==\  \    `--`\==\- \  |==|   `.-.|==|,|  / - | 
|==|_ ,    /|==|- |==|- |   /==/_ ,    /        \==\ -\   \==\  \/ -/   \==\ -\        \==\_ \/==/_ ,    /|==|  \/  , | 
|==|   .--' |==| ,|==|, |   |==|    .-'         _\==\ ,\   |==|  ,_/    _\==\ ,\       |==|- ||==|    .-' |==|- ,   _ | 
|==|-  |    |==|- |==|- `-._|==|_  ,`-._       /==/\/ _ |  \==\-, /    /==/\/ _ |      |==|, ||==|_  ,`-._|==| _ /\   | 
/==/   \    /==/. /==/ - , ,/==/ ,     /       \==\ - , /  /==/._/     \==\ - , /      /==/ -//==/ ,     //==/  / / , / 
`--`---'    `--`-``--`-----'`--`-----``         `--`---'   `--`-`       `--`---'       `--`--``--`-----`` `--`./  `--` 
"""

print(word)


class FileSystemManager:
    def create_file(self):
        file_name = input("Enter the filename or file path to save in different directory (e.g: /home/user-directory/file_name)")
        if os.path.exists(file_name):
            print("File already exists.")
        else:
             with open(file_name, 'w') as f:
                 print(f"{file_name} created successfully.")
                 

    def read_file(self):
        file_name = input("Enter the filename path (e.g: /home/user-directory/file_name)")
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                content = f.read()
                print("File content:")
                print(content)
        else:
            print(f"{file_name} not Found")
        
    def create_and_write_to_file(self):
        file_name = input("Enter the filename Path (e.g. /home/user-directory/file_name): ")
        if os.path.exists(file_name):
            print("File already exists.")
        else:
            with open(file_name, 'w') as f:
                print(f"{file_name} created successfully.")
            with open(file_name, 'a') as f:
                w_file = input(f"Enter something in {file_name}: ")
                f.write(w_file)
                print("Written data Successfully")
    

    def delete_file(self):
        file_name = input("Enter the filename (e.g: /home/user/file_name): ")
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"{file_name} deleted successfully.")
        else:
            print(f"{file_name} not found.")

    def create_directory(self):
        dir_name = input("Enter the directory name: ")
        if os.path.exists(dir_name):
            print(f"{dir_name} already exists.")
        else:
            os.mkdir(dir_name)
            print(f"{dir_name} created successfully.")

    def create_directory_create_file(self):
        dir_name = input("Enter the directory name: ")
        if os.path.exists(dir_name):
            print(f"{dir_name} already exists.")
        else:
            os.mkdir(dir_name)
            print(f"{dir_name} created successfully.")
        file_name = input("Enter the filename Path (e.g. /home/user-directory/file_name): ")
        if os.path.exists(file_name):
            print(f"{file_name} already exists.")
        else:
            with open(file_name, 'w') as f:
                print(f"{file_name} created successfully.")

    def create_directory_create_file_and_write_to_file(self):
        dir_name = input("Enter the directory name: ")
        if os.path.exists(dir_name):
            print(f"{dir_name} already exists.")
        else:
            os.mkdir(dir_name)
                print(f"{dir_name} created successfully.")
            file_name = input("Enter the filename Path (e.g. /home/user-directory/file_name): ")
            if os.path.exists(file_name):
                print(f"{file_name} already exists.")
            else:
                with open(file_name, 'w') as f:
                    print(f"{file_name} created successfully.")
                with open(file_name, 'a') as f:
                    data = input("Enter some data on file: ")
                    f.write(data)
                    print(" Data written successfully.")

        def list_files_in_directory(self):
            dir_name = input("Enter the directory name: ")
            if os.path.exists(dir_name):
                files = os.listdir(dir_name)
                print("[LIST OF FILE IN DIRECTORY]>>")
            
                for file in files:
                    print('******************P*E*R*M*I*S*S*I*O*N*S******************')
                    if os.access(file, os.R_OK):
                        print(f"\t{file} has read permissions granted.")
                    else:
                        print(f"\t{file} has read permissions not granted.")
                    if os.access(file, os.W_OK):
                        print(f"\t{file} has write permissions granted.")
                    else:
                        print(f"\t{file} has write permissions not granted.")
                    if os.access(file, os.X_OK):
                        print(f"\t{file} has execute permissions granted.")
                    else:
                        print(f"\t{file} has execute permissions not granted.")
            else:
                print("Directory not found.")

        def search_file_in_directory(self):
            dir_name = input("Enter the directory name: ")
            if os.path.exists(dir_name):
                file_name = input("Enter the filename to search: ")
                if file_name in os.listdir(dir_name):
                    print(f"{file_name} found.")
                else:
                    print(f"{file_name} not found.")
            else:
                print(f"{dir_name} not found.")

        def delete_dir(self):
            dir_name = input("Enter the name of the directory:")
            if os.path.exists(dir_name):
                os.rmdir(dir_name)
                print(f"{dir_name} has been deleted successfully.")
            else:
                print(f"{dir_name} does not exist.")

        def change_file_permissions(self, file_path, mode):
            try:
                subprocess.run(['chmod', str(mode), file_path])
                print("File permissions changed successfully.")
            except subprocess.CalledProcessError as e:
                print("Error while changing file permissions:", str(e))

        def change_perm(self):
            file_path = input("Enter the file path (eg: /home/user-directory/file_name): ")
            if os.path.exists(file_path):
                mode_input = input("Enter the new file permissions (e.g., '755', '644'): ")

                try:
                    mode = int(mode_input, 8)  # Convert octal string to integer
                    self.change_file_permissions(file_path, mode)
                except ValueError:
                    print("Invalid octal format. Please enter a valid octal number.")
            else:
                print(f"{file_path} not found.")

        def show_menu(self):
            print("File System Menu:")
            print('**************************************************************************************\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n**************************************************************************************')
            print("1. Create File")
            print("2. Read File (Implement this function if needed)")
            print("3. Write to File (Implement this function if needed)")
            print("4. Create and write to file")
            print("5. Delete File")
            print("6. Create Directory")
            print("7. Create Directory and create file")
            print("8. Create Directory and create file and write to file")
            print("9. List Files in Directory")
            print("10. Search File in Directory")
            print("11. Delete Directory")
            print("12. Change permission")
            print("13. Exit")

        def run(self):
            while True:
                try:
                    self.show_menu()
                    print("=============================================================================================")
                    choice = input("Enter your choice (1-13): ")
                    if choice == '1':
                        self.create_and_write_to_file()
                    elif choice == '2':
                        self.read_file()
                    elif choice == '3':
                        self.create_file()
                    elif choice == '4':
                        self.create_directory_create_file_and_write_to_file()
                    elif choice == '5':
                        self.delete_file()
                    elif choice == '6':
                        self.create_directory()
                    elif choice == '7':
                        self.create_directory_create_file()
                    elif choice == '8':
                        self.create_directory_create_file_and_write_to_file()
                    elif choice == '9':
                        self.list_files_in_directory()
                    elif choice == '10':
                        self.search_file_in_directory()
                    elif choice == '11':
                        self.delete_dir()
                    elif choice == '12':
                        self.change_perm()
                    elif choice == '13':
                        print("Exiting.")
                        break
                    elif choice == "KeyboardInterrupt":
                        print("hello")
                    else:
                        print("Invalid choice. Please enter a valid option.")
                except KeyboardInterrupt:
                    a = input("\nYou really wanna terminate (Y/N): ")
                    if a.lower() == "y":
                        print("Terminating...")
                        break
                    else:
                        continue
    if __name__ == "__main__":
        manager = FileSystemManager()
        manager.run()







word = r"""
   _,---.   .=-.-.             ,----.           ,-,--.                  ,-,--.  ,--.--------.    ,----.         ___   
  .-`.' ,  \ /==/_ / _.-.     ,-.--` , \        ,-.'-  _\ ,--.-.  .-,--.,-.'-  _\/==/,  -   , -\,-.--` , \ .-._ .'=.'\  
 /==/_  _.-'|==|, |.-,.'|    |==|-  _.-`       /==/_ ,_.'/==/- / /=/_ //==/_ ,_.'\==\.-.  - ,-./==|-  _.-`/==/ \|==|  | 
/==/-  '..-.|==|  |==|, |    |==|   `.-.       \==\  \   \==\, \/=/. / \==\  \    `--`\==\- \  |==|   `.-.|==|,|  / - | 
|==|_ ,    /|==|- |==|- |   /==/_ ,    /        \==\ -\   \==\  \/ -/   \==\ -\        \==\_ \/==/_ ,    /|==|  \/  , | 
|==|   .--' |==| ,|==|, |   |==|    .-'         _\==\ ,\   |==|  ,_/    _\==\ ,\       |==|- ||==|    .-' |==|- ,   _ | 
|==|-  |    |==|- |==|- `-._|==|_  ,`-._       /==/\/ _ |  \==\-, /    /==/\/ _ |      |==|, ||==|_  ,`-._|==| _ /\   | 
/==/   \    /==/. /==/ - , ,/==/ ,     /       \==\ - , /  /==/._/     \==\ - , /      /==/ -//==/ ,     //==/  / / , / 
`--`---'    `--`-``--`-----'`--`-----``         `--`---'   `--`-`       `--`---'       `--`--``--`-----`` `--`./  `--` 
"""

print(word)


class FileSystemManager:
    def create_file(self):
        file_name = input("Enter the filename or file path to save in different directory (e.g: /home/user-directory/file_name)")
        if os.path.exists(file_name):
            print("File already exists.")
        else:
             with open(file_name, 'w') as f:
                 print(f"{file_name} created successfully.")
                 

    def read_file(self):
        file_name = input("Enter the filename path (e.g: /home/user-directory/file_name)")
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                content = f.read()
                print("File content:")
                print(content)
        else:
            print(f"{file_name} not Found")
        
    def create_and_write_to_file(self):
        file_name = input("Enter the filename Path (e.g. /home/user-directory/file_name): ")
        if os.path.exists(file_name):
            print("File already exists.")
        else:
            with open(file_name, 'w') as f:
                print(f"{file_name} created successfully.")
            with open(file_name, 'a') as f:
                w_file = input(f"Enter something in {file_name}: ")
                f.write(w_file)
                print("Written data Successfully")
    

    def delete_file(self):
        file_name = input("Enter the filename (e.g: /home/user/file_name): ")
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"{file_name} deleted successfully.")
        else:
            print(f"{file_name} not found.")

    def create_directory(self):
        dir_name = input("Enter the directory name: ")
        if os.path.exists(dir_name):
            print(f"{dir_name} already exists.")
        else:
            os.mkdir(dir_name)
            print(f"{dir_name} created successfully.")

    def create_directory_create_file(self):
        dir_name = input("Enter the directory name: ")
        if os.path.exists(dir_name):
            print(f"{dir_name} already exists.")
        else:
            os.mkdir(dir_name)
            print(f"{dir_name} created successfully.")
        file_name = input("Enter the filename Path (e.g. /home/user-directory/file_name): ")
        if os.path.exists(file_name):
            print(f"{file_name} already exists.")
        else:
            with open(file_name, 'w') as f:
                print(f"{file_name} created successfully.")

    def create_directory_create_file_and_write_to_file(self):
        dir_name = input("Enter the directory name: ")
        if os.path.exists(dir_name):
            print(f"{dir_name} already exists.")
        else:
            os.mkdir(dir_name)
            print(f"{dir_name} created successfully.")
        file_name = input("Enter the filename Path (e.g. /home/user-directory/file_name): ")
        if os.path.exists(file_name):
            print(f"{file_name} already exists.")
        else:
            with open(file_name, 'w') as f:
                print(f"{file_name} created successfully.")
            with open(file_name, 'a') as f:
                data = input("Enter some data on file: ")
                f.write(data)
                print(" Data written successfully.")

    def list_files_in_directory(self):
        dir_name = input("Enter the directory name: ")
        if os.path.exists(dir_name):
            files = os.listdir(dir_name)
            print("[LIST OF FILE IN DIRECTORY]>>")
            
            for file in files:
                print('******************P*E*R*M*I*S*S*I*O*N*S******************')
                if os.access(file, os.R_OK):
                    print(f"\t{file} has read permissions granted.")
                else:
                    print(f"\t{file} has read permissions not granted.")
                if os.access(file, os.W_OK):
                    print(f"\t{file} has write permissions granted.")
                else:
                    print(f"\t{file} has write permissions not granted.")
                if os.access(file, os.X_OK):
                    print(f"\t{file} has execute permissions granted.")
                else:
                    print(f"\t{file} has execute permissions not granted.")
        else:
            print("Directory not found.")

    def search_file_in_directory(self):
        dir_name = input("Enter the directory name: ")
        if os.path.exists(dir_name):
            file_name = input("Enter the filename to search: ")
            if file_name in os.listdir(dir_name):
                print(f"{file_name} found.")
            else:
                print(f"{file_name} not found.")
        else:
            print(f"{dir_name} not found.")

    def delete_dir(self):
        dir_name = input("Enter the name of the directory:")
        if os.path.exists(dir_name):
            os.rmdir(dir_name)
            print(f"{dir_name} has been deleted successfully.")
        else:
            print(f"{dir_name} does not exist.")

    def change_file_permissions(self, file_path, mode):
        try:
            subprocess.run(['chmod', str(mode), file_path])
            print("File permissions changed successfully.")
        except subprocess.CalledProcessError as e:
            print("Error while changing file permissions:", str(e))

    def change_perm(self):
        file_path = input("Enter the file path (eg: /home/user-directory/file_name): ")
        if os.path.exists(file_path):
            mode_input = input("Enter the new file permissions (e.g., '755', '644'): ")
            try:
                mode = int(mode_input, 8)  # Convert octal string to integer
                self.change_file_permissions(file_path, mode)
            except ValueError:
                print("Invalid octal format. Please enter a valid octal number.")
        else:
            print(f"{file_path} not found.")

    def show_menu(self):
        print("File System Menu:")
        print('**************************************************************************************\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n**************************************************************************************')
        print("1. Create File")
        print("2. Read File (Implement this function if needed)")
        print("3. Write to File (Implement this function if needed)")
        print("4. Create and write to file")
        print("5. Delete File")
        print("6. Create Directory")
        print("7. Create Directory and create file")
        print("8. Create Directory and create file and write to file")
        print("9. List Files in Directory")
        print("10. Search File in Directory")
        print("11. Delete Directory")
        print("12. Change permission")
        print("13. Exit")

    def run(self):
        while True:
            try:
                self.show_menu()
                print("=============================================================================================")
                choice = input("Enter your choice (1-13): ")
                if choice == '1':
                    self.create_and_write_to_file()
                elif choice == '2':
                    self.read_file()
                elif choice == '3':
                    self.create_file()
                elif choice == '4':
                    self.create_directory_create_file_and_write_to_file()
                elif choice == '5':
                    self.delete_file()
                elif choice == '6':
                    self.create_directory()
                elif choice == '7':
                    self.create_directory_create_file()
                elif choice == '8':
                    self.create_directory_create_file_and_write_to_file()
                elif choice == '9':
                    self.list_files_in_directory()
                elif choice == '10':
                    self.search_file_in_directory()
                elif choice == '11':
                    self.delete_dir()
                elif choice == '12':
                    self.change_perm()
                elif choice == '13':
                    print("Exiting.")
                    break
                elif choice == "KeyboardInterrupt":
                    print("hello")
                else:
                    print("Invalid choice. Please enter a valid option.")
            except KeyboardInterrupt:
                a = input("\nYou really wanna terminate (Y/N): ")
                if a.lower() == "y":
                    print("Terminating...")
                    break
                else:
                    continue
if __name__ == "__main__":
    manager = FileSystemManager()
    manager.run()
