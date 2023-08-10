from simple_term_menu import TerminalMenu
import os
import subprocess
import zipfile
import time
import shutil

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
        file_name = input("Enter the filename or file path to save in a different directory (e.g: /home/user-directory/file_name): ")
        try:
            if os.path.exists(file_name):
                print("File already exists.")
            else:
                with open(file_name, 'w') as f:
                    print(f"{file_name} created successfully.")
        except Exception as e:
            print(f"Error occurred while creating the file: {str(e)}")

    def read_file(self):
        file_name = input("Enter the filename path (e.g: /home/user-directory/file_name): ")
        try:
            if os.path.exists(file_name):
                with open(file_name, 'r') as f:
                    content = f.read()
                    print("File content:")
                    print(content)
            else:
                print(f"{file_name} not Found")
        except Exception as e:
            print(f"Error occurred while reading the file: {str(e)}")

    def write_to_file(self):
        file_name = input("Enter the filename Path (e.g. /home/user-directory/file_name): ")
        try:
            if os.path.exists(file_name):
                print("File already exists.")
            else:
                with open(file_name, 'w') as f:
                    print(f"{file_name} created successfully.")
                with open(file_name, 'a') as f:
                    w_file = input(f"Enter something in {file_name}: ")
                    f.write(w_file)
                    print("Written data Successfully")
        except Exception as e:
            print(f"Error occurred while writing to the file: {str(e)}")

    def delete_file(self):
        file_name = input("Enter the filename (e.g: /home/user/file_name): ")
        try:
            if os.path.exists(file_name):
                os.remove(file_name)
                print(f"{file_name} deleted successfully.")
            else:
                print(f"{file_name} not found.")
        except Exception as e:
            print(f"Error occurred while deleting the file: {str(e)}")

    def copy_file(self):
        source_file = input("Enter the source filename path (e.g: /home/user/file_name): ")
        destination_file = input("Enter the destination filename path (e.g: /home/user/file_name): ")
        try:
            if os.path.exists(source_file):
                shutil.copy2(source_file, destination_file)
                print(f"{source_file} copied to {destination_file} successfully.")
            else:
                print(f"{source_file} not found.")
        except Exception as e:
            print(f"Error occurred while copying the file: {str(e)}")

    def move_file(self):
        source_file = input("Enter the source filename path (e.g: /home/user/file_name): ")
        destination_file = input("Enter the destination filename path (e.g: /home/user/file_name): ")
        try:
            if os.path.exists(source_file):
                shutil.move(source_file, destination_file)
                print(f"{source_file} moved to {destination_file} successfully.")
            else:
                print(f"{source_file} not found.")
        except Exception as e:
            print(f"Error occurred while moving the file: {str(e)}")

    def rename_file(self):
        source_file = input("Enter the source filename path (e.g: /home/user/file_name): ")
        new_name = input("Enter the new filename: ")
        try:
            if os.path.exists(source_file):
                os.rename(source_file, new_name)
                print(f"{source_file} renamed to {new_name} successfully.")
            else:
                print(f"{source_file} not found.")
        except Exception as e:
            print(f"Error occurred while renaming the file: {str(e)}")

    def create_directory(self):
        dir_name = input("Enter the directory name: ")
        try:
            if os.path.exists(dir_name):
                print(f"{dir_name} already exists.")
            else:
                os.mkdir(dir_name)
                print(f"{dir_name} created successfully.")
        except Exception as e:
            print(f"Error occurred while creating the directory: {str(e)}")

    def create_directory_create_file(self):
        dir_name = input("Enter the directory name: ")
        try:
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
        except Exception as e:
            print(f"Error occurred while creating the directory or file: {str(e)}")

    def create_directory_create_file_and_write_to_file(self):
        dir_name = input("Enter the directory name: ")
        try:
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
                        data = input("Enter some data in the file: ")
                        f.write(data)
                        print("Data written successfully.")
        except Exception as e:
            print(f"Error occurred while creating the directory, file, or writing data: {str(e)}")

    def list_files_in_directory(self):
        dir_name = input("Enter the directory name: ")
        try:
            if os.path.exists(dir_name):
                files = os.listdir(dir_name)
                print(f"[LIST OF FILES IN DIRECTORY: {dir_name}]>>")
                for file in files:
                    print('******************P*E*R*M*I*S*S*I*O*N*S******************')
                    file_path = os.path.join(dir_name, file)
                    if os.access(file_path, os.R_OK):
                        print(f"\t{file} has read permissions granted.")
                    else:
                        print(f"\t{file} has read permissions not granted.")
                    if os.access(file_path, os.W_OK):
                        print(f"\t{file} has write permissions granted.")
                    else:
                        print(f"\t{file} has write permissions not granted.")
                    if os.access(file_path, os.X_OK):
                        print(f"\t{file} has execute permissions granted.")
                    else:
                        print(f"\t{file} has execute permissions not granted.")
            else:
                print("Directory not found.")
        except Exception as e:
            print(f"Error occurred while listing files in the directory: {str(e)}")

    def search_file_in_directory(self):
        dir_name = input("Enter the directory name: ")
        try:
            if os.path.exists(dir_name):
                file_name = input("Enter the filename to search: ")
                if file_name in os.listdir(dir_name):
                    print(f"{file_name} found.")
                else:
                    print(f"{file_name} not found.")
            else:
                print(f"{dir_name} not found.")
        except Exception as e:
            print(f"Error occurred while searching for the file: {str(e)}")

    def delete_dir(self):
        dir_name = input("Enter the name of the directory:")
        try:
            if os.path.exists(dir_name):
                os.rmdir(dir_name)
                print(f"{dir_name} has been deleted successfully.")
            else:
                print(f"{dir_name} does not exist.")
        except Exception as e:
            print(f"Error occurred while deleting the directory: {str(e)}")

    def change_file_permissions(self, file_path, mode):
        try:
            subprocess.run(['chmod', str(mode), file_path])
            print("File permissions changed successfully.")
        except Exception as e:
            print(f"Error occurred while changing file permissions: {str(e)}")

    def change_owner(self, file_path, owner):
        try:
            subprocess.run(['chown', owner, file_path])
            print(f"File owner changed to {owner} successfully.")
        except Exception as e:
            print(f"Error occurred while changing file owner: {str(e)}")

    def change_perm_and_owner(self):
        file_path = input("Enter the file path (e.g: /home/user-directory/file_name): ")
        try:
            if os.path.exists(file_path):
                mode_input = input("Enter the new file permissions (e.g., '755', '644'): ")
                try:
                    mode = int(mode_input, 8)  # Convert octal string to integer
                    owner = input("Enter the new file owner (e.g., 'user:group'): ")
                    self.change_file_permissions(file_path, mode)
                    self.change_owner(file_path, owner)
                except ValueError:
                    print("Invalid octal format. Please enter a valid octal number.")
            else:
                print(f"{file_path} not found.")
        except Exception as e:
            print(f"Error occurred while changing file permissions or owner: {str(e)}")

    def compress_file_or_directory(self):
        file_path = input("Enter the file or directory path to compress: ")
        try:
            if os.path.exists(file_path):
                shutil.make_archive(file_path, 'zip', file_path)
                print(f"{file_path} compressed successfully.")
            else:
                print(f"{file_path} not found.")
        except Exception as e:
            print(f"Error occurred while compressing the file or directory: {str(e)}")

    def decompress_zip_file(self):
        zip_file = input("Enter the ZIP file path to decompress: ")
        try:
            if os.path.exists(zip_file):
                shutil.unpack_archive(zip_file, os.path.dirname(zip_file))
                print(f"{zip_file} decompressed successfully.")
            else:
                print(f"{zip_file} not found.")
        except Exception as e:
            print(f"Error occurred while decompressing the ZIP file: {str(e)}")

    def file_search(self):
        keyword = input("Enter the keyword to search for in files: ")
        if not keyword:
            print("Invalid keyword. Please provide a valid keyword.")
            return

        dir_name = input("Enter the directory name to search in: ")
        if not dir_name:
            print("Invalid directory name. Please provide a valid directory name.")
            return

        try:
            if os.path.exists(dir_name):
                found_files = []
                for root, _, files in os.walk(dir_name):
                    for file in files:
                        file_path = os.path.join(root, file)
                        if keyword in file:
                            found_files.append(file_path)

                if found_files:
                    print(f"Found {len(found_files)} files containing the keyword '{keyword}' in {dir_name}:")
                    for file_path in found_files:
                        print(file_path)
                else:
                    print(f"No files containing the keyword '{keyword}' found in {dir_name}.")
            else:
                print(f"{dir_name} not found.")
        except Exception as e:
            print(f"Error occurred while searching for the keyword: {str(e)}")

    def sort_files_in_directory(self):
        dir_name = input("Enter the directory name: ")
        if not dir_name:
            print("Invalid directory name. Please provide a valid directory name.")
            return

        try:
            if os.path.exists(dir_name):
                sort_by = input("Sort by (name/size/modification_time): ")
                if sort_by not in ["name", "size", "modification_time"]:
                    print("Invalid sort criteria. Please choose 'name', 'size', or 'modification_time'.")
                    return

                files = os.listdir(dir_name)
                files.sort(key=lambda x: os.path.getsize(os.path.join(dir_name, x)) if sort_by == "size" else
                           os.path.getmtime(os.path.join(dir_name, x)) if sort_by == "modification_time" else x)
                print("[SORTED FILES IN DIRECTORY]>>")
                for file in files:
                    print(file)
            else:
                print("Directory not found.")
        except Exception as e:
            print(f"Error occurred while sorting files: {str(e)}")

    def set_metadata(self):
        path = input("Enter the file/directory path: ")
        if not path:
            print("Invalid path. Please provide a valid path.")
            return

        metadata = input("Enter metadata (e.g., tags, categories, etc.): ")
        if not metadata:
            print("Invalid metadata. Please provide valid metadata.")
            return

        try:
            if os.path.exists(path):
                # Save metadata to a separate file or database associated with the file/directory
                # Here, we are just printing the metadata for demonstration purposes.
                print(f"Metadata set for {path}: {metadata}")
            else:
                print(f"{path} not found.")
        except Exception as e:
            print(f"Error occurred while setting metadata: {str(e)}")

    def show_main_menu(self):
        main_menu_title = "luminaFS - Main Menu"
        main_menu_items = [
            "File Operations",
            "Directory Operations",
            "File Permissions and Ownership",
            "File Compression and Decompression",
            "File Search and Sorting",
            "File Metadata",
            "Exit"
        ]
        while True:
            print(main_menu_title)
            terminal_main_menu = TerminalMenu(main_menu_items, cycle_cursor=True)
            selected_main_index = terminal_main_menu.show()

            if selected_main_index == 0:
                self.show_file_ops_menu()
            elif selected_main_index == 1:
                self.show_directory_ops_menu()
            elif selected_main_index == 2:
                self.show_perm_menu()
            elif selected_main_index == 3:
                self.show_compression_menu()
            elif selected_main_index == 4:
                self.show_search_sort_menu()
            elif selected_main_index == 5:
                self.show_metadata_menu()
            elif selected_main_index == 6:
                print("Exiting.")
                time.sleep(1)
                break

    def show_file_ops_menu(self):
        file_ops_menu_title = "luminaFS - File Operations"
        file_ops_menu_items = [
            "Create File",
            "Read File",
            "Write to File",
            "Delete File",
            "Copy File",
            "Move File",
            "Rename File",
            "Back to Main Menu"
        ]
        terminal_file_ops_menu = TerminalMenu(file_ops_menu_items, menu_title=file_ops_menu_title, cycle_cursor=True)
        selected_file_ops_index = terminal_file_ops_menu.show()
        return selected_file_ops_index

    def show_directory_ops_menu(self):
        directory_ops_menu_title = "luminaFS - Directory Operations"
        directory_ops_menu_items = [
            "Create Directory",
            "Create Directory + Create File",
            "Create Directory + Create & Write File",
            "List Files in Directory",
            "Search File in Directory",
            "Delete Directory",
            "Back to Main Menu"
        ]
        terminal_directory_ops_menu = TerminalMenu(directory_ops_menu_items, menu_title=directory_ops_menu_title, cycle_cursor=True)
        selected_directory_ops_index = terminal_directory_ops_menu.show()
        return selected_directory_ops_index

    def show_perm_menu(self):
        perm_menu_title = "luminaFS - File Permissions and Ownership"
        perm_menu_items = [
            "Change File Permissions and Ownership",
            "Back to Main Menu"
        ]
        terminal_perm_menu = TerminalMenu(perm_menu_items, menu_title=perm_menu_title, cycle_cursor=True)
        selected_perm_index = terminal_perm_menu.show()
        return selected_perm_index

    def show_compression_menu(self):
        compress_menu_title = "luminaFS - File Compression and Decompression"
        compress_menu_items = [
            "Compress File/Directory (ZIP)",
            "Decompress ZIP File",
            "Back to Main Menu"
        ]
        terminal_compress_menu = TerminalMenu(compress_menu_items, menu_title=compress_menu_title, cycle_cursor=True)
        selected_compress_index = terminal_compress_menu.show()
        return selected_compress_index

    def show_search_sort_menu(self):
        search_sort_menu_title = "luminaFS - File Search and Sorting"
        search_sort_menu_items = [
            "Search for Files by Keyword",
            "Sort Files in Directory",
            "Back to Main Menu"
        ]
        terminal_search_sort_menu = TerminalMenu(search_sort_menu_items, menu_title=search_sort_menu_title, cycle_cursor=True)
        selected_search_sort_index = terminal_search_sort_menu.show()
        return selected_search_sort_index

    def show_metadata_menu(self):
        metadata_menu_title = "luminaFS - File Metadata"
        metadata_menu_items = [
            "Set Metadata for File/Directory",
            "Back to Main Menu"
        ]
        terminal_metadata_menu = TerminalMenu(metadata_menu_items, menu_title=metadata_menu_title, cycle_cursor=True)
        selected_metadata_index = terminal_metadata_menu.show()
        return selected_metadata_index

    def run(self):
        while True:
            try:
                selected_main_index = self.show_main_menu()

                if selected_main_index == 0:
                    while True:
                        selected_file_ops_index = self.show_file_ops_menu()
                        if selected_file_ops_index == 0:
                            self.create_file()
                        elif selected_file_ops_index == 1:
                            self.read_file()
                        elif selected_file_ops_index == 2:
                            self.write_to_file()
                        elif selected_file_ops_index == 3:
                            self.delete_file()
                        elif selected_file_ops_index == 4:
                            self.copy_file()
                        elif selected_file_ops_index == 5:
                            self.move_file()
                        elif selected_file_ops_index == 6:
                            self.rename_file()
                        elif selected_file_ops_index == 7:
                            break

                elif selected_main_index == 1:
                    while True:
                        selected_directory_ops_index = self.show_directory_ops_menu()
                        if selected_directory_ops_index == 0:
                            self.create_directory()
                        elif selected_directory_ops_index == 1:
                            self.create_directory_create_file()
                        elif selected_directory_ops_index == 2:
                            self.create_directory_create_file_and_write_to_file()
                        elif selected_directory_ops_index == 3:
                            self.list_files_in_directory()
                        elif selected_directory_ops_index == 4:
                            self.search_file_in_directory()
                        elif selected_directory_ops_index == 5:
                            self.delete_dir()
                        elif selected_directory_ops_index == 6:
                            break

                elif selected_main_index == 2:
                    while True:
                        selected_perm_index = self.show_perm_menu()
                        if selected_perm_index == 0:
                            self.change_perm_and_owner()
                        elif selected_perm_index == 1:
                            break

                elif selected_main_index == 3:
                    while True:
                        selected_compress_index = self.show_compression_menu()
                        if selected_compress_index == 0:
                            self.compress_file_or_directory()
                        elif selected_compress_index == 1:
                            self.decompress_zip_file()
                        elif selected_compress_index == 2:
                            break

                elif selected_main_index == 4:
                    while True:
                        selected_search_sort_index = self.show_search_sort_menu()
                        if selected_search_sort_index == 0:
                            self.file_search()
                        elif selected_search_sort_index == 1:
                            self.sort_files_in_directory()
                        elif selected_search_sort_index == 2:
                            break

                elif selected_main_index == 5:
                    while True:
                        selected_metadata_index = self.show_metadata_menu()
                        if selected_metadata_index == 0:
                            self.set_metadata()
                        elif selected_metadata_index == 1:
                            break

                elif selected_main_index == 6:
                    print("Exiting.")
                    time.sleep(1)
                    break

            except KeyboardInterrupt:
                a = input("\nYou really want to terminate (Y/N): ")
                if a.lower() == "y":
                    print("Terminating...")
                    time.sleep(1)
                    break
                else:
                    continue


if __name__ == "__main__":
    manager = FileSystemManager()
    manager.run()
