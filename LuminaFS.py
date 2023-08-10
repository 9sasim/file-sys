import os
import subprocess
import zipfile
import shutil
import time
import signal
from simple_term_menu import TerminalMenu

luminafs_ascii = r"""
 .----------------. .----------------. .----------------. .----------------. .-----------------..----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |   _____      | | | _____  _____ | | | ____    ____ | | |     _____    | | | ____  _____  | | |      __      | | |  _________   | | |    _______   | |
| |  |_   _|     | | ||_   _||_   _|| | ||_   \  /   _|| | |    |_   _|   | | ||_   \|_   _| | | |     /  \     | | | |_   ___  |  | | |   /  ___  |  | |
| |    | |       | | |  | |    | |  | | |  |   \/   |  | | |      | |     | | |  |   \ | |   | | |    / /\ \    | | |   | |_  \_|  | | |  |  (__ \_|  | |
| |    | |   _   | | |  | '    ' |  | | |  | |\  /| |  | | |      | |     | | |  | |\ \| |   | | |   / ____ \   | | |   |  _|      | | |   '.___`-.   | |
| |   _| |__/ |  | | |   \ `--' /   | | | _| |_\/_| |_ | | |     _| |_    | | | _| |_\   |_  | | | _/ /    \ \_ | | |  _| |_       | | |  |`\____) |  | |
| |  |________|  | | |    `.__.'    | | ||_____||_____|| | |    |_____|   | | ||_____|\____| | | ||____|  |____|| | | |_____|      | | |  |_______.'  | |
| |              | | |              | | |              | | |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' 
"""

print(luminafs_ascii)


class FileSystemManager:

    def create_file(self):
        try:
            file_name = input("Enter the filename or file path to save in a different directory (e.g: /home/user-directory/file_name): ")
            if os.path.exists(file_name):
                print("File already exists.")
            else:
                with open(file_name, 'w') as f:
                    print(f"{file_name} created successfully.")
        except KeyboardInterrupt:
            print("\nFile creation interrupted by user.")

    def read_file(self):
        try:
            file_name = input("Enter the filename path (e.g: /home/user-directory/file_name): ")
            
            with open(file_name, 'r') as f:
                content = f.read()
                print("File content:")
                print(content)
        except FileNotFoundError:
                print(f"{file_name} not Found")
        except FileExistsError:
            print("{file_name} you enter have some kind of fault")
        except KeyboardInterrupt:
            print("\nReading file interrupted by user.")
        except PermissionError:
            print(f"{file_name} didn't have read permssison on the current user")

    def write_to_file(self):
        try:
            file_name = input("Enter the filename path (e.g. /home/user-directory/file_name): ")
            if os.path.exists(file_name):
                with open(file_name, 'a') as f:
                    w_file = input(f"Enter something in {file_name}: ")
                    f.write(w_file)
                    print("Written data Successfully")
            else:
                print(f"{file_name} not found.")
        except KeyboardInterrupt:
            print("\nWriting to file interrupted by user.")

    def delete_file(self):
        try:
            file_name = input("Enter the filename (e.g: /home/user/file_name): ")
            if os.path.exists(file_name):
                os.remove(file_name)
                print(f"{file_name} deleted successfully.")
            else:
                print(f"{file_name} not found.")
        except KeyboardInterrupt:
            print("\nFile deletion interrupted by user.")

    def copy_file(self):
        try:
            src_file = input("Enter the source file path: ")
            if os.path.exists(src_file):
                dst_file = input("Enter the destination file path: ")
                if not os.path.exists(dst_file):
                    shutil.copy(src_file, dst_file)
                    print(f"{src_file} copied to {dst_file} successfully.")
                else:
                    print(f"{dst_file} already exists.")
            else:
                print(f"{src_file} not found.")
        except KeyboardInterrupt:
            print("\nFile copying interrupted by user.")

    def move_file(self):
        try:
            src_file = input("Enter the source file path: ")
            if os.path.exists(src_file):
                dst_file = input("Enter the destination file path: ")
                if not os.path.exists(dst_file):
                    shutil.move(src_file, dst_file)
                    print(f"{src_file} moved to {dst_file} successfully.")
                else:
                    print(f"{dst_file} already exists.")
            else:
                print(f"{src_file} not found.")
        except KeyboardInterrupt:
            print("\nFile moving interrupted by user.")

    def rename_file(self):
        try:
            old_name = input("Enter the old filename: ")
            if not old_name:
                print("Invalid old name. Please provide a valid name.")
                return

            new_name = input("Enter the new filename: ")
            if not new_name:
                print("Invalid new name. Please provide a valid name.")
                return

            if os.path.exists(old_name):
                os.rename(old_name, new_name)
                print(f"{old_name} has been renamed to {new_name} successfully.")
            else:
                print(f"{old_name} not found.")
        except KeyboardInterrupt:
            print("\nFile renaming interrupted by user.")

    def create_directory(self):
        try:
            dir_name = input("Enter the directory name: ")
            if os.path.exists(dir_name):
                print(f"{dir_name} already exists.")
            else:
                os.mkdir(dir_name)
                print(f"{dir_name} created successfully.")
        except KeyboardInterrupt:
            print("\nDirectory creation interrupted by user.")

    def create_directory_create_file(self):
        try:
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
        except KeyboardInterrupt:
            print("\nDirectory and file creation interrupted by user.")

    def create_directory_create_file_and_write_to_file(self):
        try:
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
                    print("Data written successfully.")
        except KeyboardInterrupt:
            print("\nDirectory, file creation, and data writing interrupted by user.")

    def list_files_in_directory(self):
        try:
            dir_name = input("Enter the directory name: ")
            if os.path.exists(dir_name):
                files = os.listdir(dir_name)
                print("[LIST OF FILE IN DIRECTORY]>>")
                for file in files:
                    print(file)
            else:
                print("Directory not found.")
        except KeyboardInterrupt:
            print("\nListing files interrupted by user.")

    def search_file_in_directory(self):
        try:
            dir_name = input("Enter the directory name: ")
            if os.path.exists(dir_name):
                file_name = input("Enter the filename to search: ")
                if file_name in os.listdir(dir_name):
                    print(f"{file_name} found.")
                else:
                    print(f"{file_name} not found.")
            else:
                print(f"{dir_name} not found.")
        except KeyboardInterrupt:
            print("\nFile search interrupted by user.")

    def delete_dir(self):
        try:
            dir_name = input("Enter the name of the directory:")
            if os.path.exists(dir_name):
                os.rmdir(dir_name)
                print(f"{dir_name} has been deleted successfully.")
            else:
                print(f"{dir_name} does not exist.")
        except KeyboardInterrupt:
            print("\nDirectory deletion interrupted by user.")

    def list_permission_and_owner(self):
        try:
            dir_path = input("Enter the directory path (e.g. /home/user-directory): ")
            if os.path.exists(dir_path):
                for root, _, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        file_stat = os.stat(file_path)
                        permissions = oct(file_stat.st_mode)[-3:]  # Convert permission mode to octal string
                        owner = file_stat.st_uid
                        owner_name = os.path.basename(os.path.expanduser("~"))
                        owner_group = os.path.basename(os.path.expanduser("~"))

                        print(f"File Permissions: {permissions}")
                        print(f"Owner: {owner_name} ({owner})")
                        print(f"Group: {owner_group}")
                        print(f"Path: {file_path}")
                        print()

                    for dir in os.listdir(root):
                        dir_path = os.path.join(root, dir)
                        dir_stat = os.stat(dir_path)
                        permissions = oct(dir_stat.st_mode)[-3:]  # Convert permission mode to octal string
                        owner = dir_stat.st_uid
                        owner_name = os.path.basename(os.path.expanduser("~"))
                        owner_group = os.path.basename(os.path.expanduser("~"))

                        print(f"Directory Permissions: {permissions}")
                        print(f"Owner: {owner_name} ({owner})")
                        print(f"Group: {owner_group}")
                        print(f"Path: {dir_path}")
                        print()

            else:
                print(f"{dir_path} not found.")
        except KeyboardInterrupt:
            print("\nListing permissions and owners interrupted by user.")

    def change_file_permissions(self, file_path, mode):
        try:
            subprocess.run(['chmod', str(mode), file_path])
            print("File permissions changed successfully.")
        except subprocess.CalledProcessError as e:
            print("Error while changing file permissions:", str(e))

    def change_file_ownership(self, file_path, owner, group):
        try:
            subprocess.run(['chown', f"{owner}:{group}", file_path])
            print("File ownership changed successfully.")
        except subprocess.CalledProcessError as e:
            print("Error while changing file ownership:", str(e))

    def change_perm_and_owner(self):
        try:
            file_path = input("Enter the file path (eg: /home/user-directory/file_name): ")
            if os.path.exists(file_path):
                mode_input = input("Enter the new file permissions (e.g., '755', '644'): ")
                try:
                    mode = int(mode_input, 8)  # Convert octal string to integer
                    self.change_file_permissions(file_path, mode)

                    owner = input("Enter the new owner: ")
                    group = input("Enter the new group: ")
                    self.change_file_ownership(file_path, owner, group)
                except ValueError:
                    print("Invalid octal format. Please enter a valid octal number.")
            else:
                print(f"{file_path} not found.")
        except KeyboardInterrupt:
            print("\nChanging permissions and owner interrupted by user.")

    def compress_file_or_directory(self):
        try:
            file_path = input("Enter the file/directory path to compress: ")
            if os.path.exists(file_path):
                zip_name = input("Enter the ZIP file name to create: ")
                if not os.path.exists(zip_name):
                    with zipfile.ZipFile(zip_name, 'w') as zipf:
                        if os.path.isdir(file_path):
                            for root, dirs, files in os.walk(file_path):
                                for file in files:
                                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), file_path))
                        else:
                            zipf.write(file_path, os.path.basename(file_path))
                    print(f"{file_path} compressed to {zip_name} successfully.")
                else:
                    print(f"{zip_name} already exists.")
            else:
                print(f"{file_path} not found.")
        except KeyboardInterrupt:
            print("\nCompression interrupted by user.")

    def extract_zip(self):
        try:
            zip_name = input("Enter the ZIP file path to extract: ")
            if os.path.exists(zip_name):
                with zipfile.ZipFile(zip_name, 'r') as zipf:
                    zipf.extractall()
                print(f"{zip_name} extracted successfully.")
            else:
                print(f"{zip_name} not found.")
        except KeyboardInterrupt:
            print("\nExtraction interrupted by user.")

    def exit_program(self):
        print("Exiting LuminaFS...")
        time.sleep(1)
        exit()


def main():
    file_system_manager = FileSystemManager()
    options = [
        "Create a File",
        "Read a File",
        "Write to a File",
        "Delete a File",
        "Copy a File",
        "Move a File",
        "Rename a File",
        "Create a Directory",
        "Create a Directory and File",
        "Create a Directory, File, and Write to File",
        "List Files in Directory",
        "Search File in Directory",
        "Delete a Directory",
        "List Permission and Owner",
        "Change File Permissions and Owner",
        "Compress File or Directory",
        "Extract ZIP",
        "Exit"
    ]

    while True:
        terminal_menu = TerminalMenu(options, title="LuminaFS - Simple File System Management")
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == 0:
            file_system_manager.create_file()
        elif menu_entry_index == 1:
            file_system_manager.read_file()
        elif menu_entry_index == 2:
            file_system_manager.write_to_file()
        elif menu_entry_index == 3:
            file_system_manager.delete_file()
        elif menu_entry_index == 4:
            file_system_manager.copy_file()
        elif menu_entry_index == 5:
            file_system_manager.move_file()
        elif menu_entry_index == 6:
            file_system_manager.rename_file()
        elif menu_entry_index == 7:
            file_system_manager.create_directory()
        elif menu_entry_index == 8:
            file_system_manager.create_directory_create_file()
        elif menu_entry_index == 9:
            file_system_manager.create_directory_create_file_and_write_to_file()
        elif menu_entry_index == 10:
            file_system_manager.list_files_in_directory()
        elif menu_entry_index == 11:
            file_system_manager.search_file_in_directory()
        elif menu_entry_index == 12:
            file_system_manager.delete_dir()
        elif menu_entry_index == 13:
            file_system_manager.list_permission_and_owner()
        elif menu_entry_index == 14:
            file_system_manager.change_perm_and_owner()
        elif menu_entry_index == 15:
            file_system_manager.compress_file_or_directory()
        elif menu_entry_index == 16:
            file_system_manager.extract_zip()
        elif menu_entry_index == 17:
            file_system_manager.exit_program()


if __name__ == "__main__":
    main()
