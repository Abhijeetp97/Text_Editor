import os

def show_menu():
    """
    Display the menu options.
    """
    print("\nSimple Text Editor")
    print("1. Open an existing file")
    print("2. Create a new file")
    print("3. Search and replace")
    print("4. Undo last change")
    print("5. Redo last undone change")
    print("6. Exit")

def open_file():
    """
    Open an existing text file and return its content.
    """
    filename = input("Enter the filename to open: ").strip()
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Opened file '{filename}'.")
        return filename, content
    else:
        print(f"File '{filename}' not found.")
        return None, ""

def create_file():
    """
    Create a new text file and return its name.
    """
    filename = input("Enter the filename to create: ").strip()
    if os.path.exists(filename):
        print(f"File '{filename}' already exists.")
    else:
        with open(filename, 'w') as file:
            pass
        print(f"Created new file '{filename}'.")
    return filename, ""

def save_file(filename, content, mode='w'):
    """
    Save the content to the specified file.
    """
    with open(filename, mode) as file:
        file.write(content)
    print(f"Saved file '{filename}'.")

def edit_content(content, append=False):
    """
    Edit the content of the file.
    """
    if append:
        print("Appending to the file. Enter your text (type 'SAVE' to save and exit):")
    else:
        print("Overwriting the file. Enter your text (type 'SAVE' to save and exit):")
    
    while True:
        line = input()
        if line.strip().upper() == 'SAVE':
            break
        content += line + "\n"
    return content

def search_replace(content):
    """
    Search for specific words or phrases in the text and replace them with new content.
    """
    search_term = input("Enter the word or phrase to search for: ").strip()
    replace_term = input("Enter the new word or phrase to replace with: ").strip()
    if search_term in content:
        content = content.replace(search_term, replace_term)
        print(f"Replaced all occurrences of '{search_term}' with '{replace_term}'.")
    else:
        print(f"'{search_term}' not found in the content.")
    return content

def main():
    """
    Main function to run the Simple Text Editor application.
    """
    history = []
    redo_stack = []
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()
        if choice == '1':
            filename, content = open_file()
            if filename:
                mode = input("Do you want to overwrite (O) or append (A) the file? ").strip().upper()
                if mode == 'A':
                    content = edit_content(content, append=True)
                    save_file(filename, content, mode='a')
                elif mode == 'O':
                    content = edit_content("", append=False)
                    save_file(filename, content)
                else:
                    print("Invalid choice. Please enter 'O' for overwrite or 'A' for append.")
            history.append(content)
        elif choice == '2':
            filename, content = create_file()
            content = edit_content("")
            save_file(filename, content)
            history.append(content)
        elif choice == '3':
            filename, content = open_file()
            if filename:
                content = search_replace(content)
                save_file(filename, content)
            history.append(content)
        elif choice == '4':
            if history:
                redo_stack.append(history.pop())
                if history:
                    content = history[-1]
                    print("Undo successful.")
                else:
                    content = ""
                    print("Nothing to undo.")
            else:
                print("Nothing to undo.")
        elif choice == '5':
            if redo_stack:
                history.append(redo_stack.pop())
                content = history[-1]
                print("Redo successful.")
            else:
                print("Nothing to redo.")
        elif choice == '6':
            print("Exiting the Simple Text Editor. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()