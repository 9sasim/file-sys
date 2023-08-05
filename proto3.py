from simple_term_menu import TerminalMenu
import os
import subprocess
import zipfile
import time

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
        if os.path.exists(file_name):
            print("File already exists.")
        else:
            with open(file_name, 'w') as f:
                print(f"{file_name} created successfully.")

    def read_file(self):
        file_name = input("Enter the filename path (e.g: /home/user-directory/file_name): ")
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                content = f.read()
                print("File content:")
                print(content)
        else:
            print(f"{file_name} not Found")

    def write_to_file(self):
        file_name = input("Enter the filename path (e.g. /home/user-directory/file_name): ")
        if os.path.exists(file_name):
            with open(file_name, 'a') as f:
                w_file = input(f"Enter something in {file_name}: ")
                f.write(w_file)
                print("Written data Successfully")
        else:
            print(f"{file_name} not found.")

    def delete_file(self):
        file_name = input("Enter the filename (e.g: /home/user/file_name): ")
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"{file_name} deleted successfully.")
        else:
            print(f"{file_name} not found.")

    def copy_file(self):
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

    def move_file(self):
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

    def rename_file(self):
        old_name = input("Enter the old filename: ")
        if not old_name:
            print("Invalid old name. Please provide a valid name.")
            return

        new_name = input("Enter the new filename: ")
        if not new_name:
            print("Invalid new name. Please provide a valid name.")
            return

        try:
            if os.path.exists(old_name):
                os.rename(old_name, new_name)
                print(f"{old_name} has been renamed to {new_name} successfully.")
            else:
                print(f"{old_name} not found.")
        except Exception as e:
            print(f"Error occurred while renaming: {str(e)}")

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
                print(file)
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

    def change_file_ownership(self, file_path, owner, group):
        try:
            subprocess.run(['chown', f"{owner}:{group}", file_path])
            print("File ownership changed successfully.")
        except subprocess.CalledProcessError as e:
            print("Error while changing file ownership:", str(e))

    def change_perm_and_owner(self):
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

    def compress_file_or_directory(self):
        file_path = input("Enter the file/directory path to compress: ")
        if os.path.exists(file_path):
            zip_name = input("Enter the ZIP file name to create: ")
            if not os.path.exists(zip_name):
                with zipfile.ZipFile(zip_name, 'w') as zipf:
                    if os.path.isdir(file_path):
                        for root, dirs, files in os.walk(file_path):
                            for file in files:
                                zipf.write(os.path.join(root, file))
                    else:
                        zipf.write(file_path)
                print(f"{file_path} compressed to {zip_name} successfully.")
            else:
                print(f"{zip_name} already exists.")
        else:
            print(f"{file_path} not found.")

    def decompress_zip_file(self):
        zip_name = input("Enter the ZIP file path to decompress: ")
        if os.path.exists(zip_name) and zipfile.is_zipfile(zip_name):
            extract_path = input("Enter the path to extract ZIP contents: ")
            if not os.path.exists(extract_path):
                os.makedirs(extract_path)
            with zipfile.ZipFile(zip_name, 'r') as zipf:
                zipf.extractall(extract_path)
            print(f"{zip_name} decompressed to {extract_path} successfully.")
        else:
            print(f"{zip_name} not found or not a valid ZIP file.")

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
