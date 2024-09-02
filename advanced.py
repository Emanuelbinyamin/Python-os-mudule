
import os

def display_menu():
    print("\n===== OS Module Application =====")
    print("1. View Current Directory")
    print("2. List Files in Directory")
    print("3. Create a New File")
    print("4. Delete a File")
    print("5. Change Directory")
    print("6. Make a New Directory")
    print("7. Remove a Directory")
    print("8. Exit")
    print("=================================")

def view_current_directory():
    print("\nCurrent Directory:", os.getcwd())

def list_files_in_directory():
    path = input("Enter directory path (leave empty for current directory): ")
    if not path:
        path = os.getcwd()
    try:
        files = os.listdir(path)
        print("\nFiles in", path, ":")
        for file in files:
            print(file)
    except FileNotFoundError:
        print("Directory not found!")

def create_new_file():
    filename = input("Enter the name of the new file (e.g., newfile.txt): ")
    try:
        with open(filename, 'w') as f:
            print("File created successfully!")
    except Exception as e:
        print("Error creating file:", e)

def delete_file():
    filename = input("Enter the name of the file to delete: ")
    try:
        os.remove(filename)
        print("File deleted successfully!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("Error deleting file:", e)

def change_directory():
    new_path = input("Enter the new directory path: ")
    try:
        os.chdir(new_path)
        print("Directory changed successfully!")
    except FileNotFoundError:
        print("Directory not found!")
    except Exception as e:
        print("Error changing directory:", e)

def make_new_directory():
    dirname = input("Enter the name of the new directory: ")
    try:
        os.makedirs(dirname)
        print("Directory created successfully!")
    except FileExistsError:
        print("Directory already exists!")
    except Exception as e:
        print("Error creating directory:", e)

def remove_directory():
    dirname = input("Enter the name of the directory to remove: ")
    try:
        os.rmdir(dirname)
        print("Directory removed successfully!")
    except FileNotFoundError:
        print("Directory not found!")
    except OSError:
        print("Directory is not empty!")
    except Exception as e:
        print("Error removing directory:", e)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            view_current_directory()
        elif choice == '2':
            list_files_in_directory()
        elif choice == '3':
            create_new_file()
        elif choice == '4':
            delete_file()
        elif choice == '5':
            change_directory()
        elif choice == '6':
            make_new_directory()
        elif choice == '7':
            remove_directory()
        elif choice == '8':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
