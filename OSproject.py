import os

def create_file(file_name):
    try:
        with open(file_name, 'x') as f:
            print(f"{file_name} has been created successfully.")
    except FileExistsError:
        print(f"{file_name} already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to view all files
def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found.")
    else:
        print("Files in the directory:")
        for file in files:
            print(file)

# Function to delete a file
def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"{file_name} has been deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to read a file
def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            content = f.read()
            print(f"Content of {file_name}:\n{content}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to edit a file
def edit_file(file_name):
    try:
        with open(file_name, 'a') as f:
            data = input("Enter data to add: ")
            f.write(data + "\n")
            print(f"Content added to {file_name} successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    while True:
        print("\nFile Management App")
        print("1. Create File")
        print("2. View All Files")
        print("3. Delete File")
        print("4. Read File")
        print("5. Edit File")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            file_name = input("Enter the file name to create: ")
            create_file(file_name)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            file_name = input("Enter the name of the file you want to delete: ")
            delete_file(file_name)
        elif choice == '4':
            file_name = input("Enter the file name to read: ")
            read_file(file_name)
        elif choice == '5':
            file_name = input("Enter the file name to edit: ")
            edit_file(file_name)
        elif choice == '6':
            print("Closing the app.")
            break
        else:
            print("Invalid number. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
