import os

def create_file():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'w') as f:
            pass
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

def delete_file():
    filename = input("Enter the filename: ")
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

def rename_file():
    old_filename = input("Enter the old filename: ")
    new_filename = input("Enter the new filename: ")
    try:
        os.rename(old_filename, new_filename)
        print(f"File '{old_filename}' renamed to '{new_filename}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

def create_directory():
    directory_name = input("Enter the directory name: ")
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

def delete_directory():
    directory_name = input("Enter the directory name: ")
    try:
        os.rmdir(directory_name)
        print(f"Directory '{directory_name}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

def rename_directory():
    old_directory_name = input("Enter the old directory name: ")
    new_directory_name = input("Enter the new directory name: ")
    try:
        os.rename(old_directory_name, new_directory_name)
        print(f"Directory '{old_directory_name}' renamed to '{new_directory_name}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

def list_files():
    files_and_dirs = os.listdir()
    print("Files and directories:")
    for item in sorted(files_and_dirs):
        print(item)

def main():
    while True:
        print("\nFile Manager Menu:")
        print("1. Create file")
        print("2. Delete file")
        print("3. Rename file")
        print("4. Create directory")
        print("5. Delete directory")
        print("6. Rename directory")
        print("7. List files and directories")
        print("8. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_file()
        elif choice == "2":
            delete_file()
        elif choice == "3":
            rename_file()
        elif choice == "4":
            create_directory()
        elif choice == "5":
            delete_directory()
        elif choice == "6":
            rename_directory()
        elif choice == "7":
            list_files()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()