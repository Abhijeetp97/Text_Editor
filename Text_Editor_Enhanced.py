import os
import json
from datetime import datetime
from typing import List, Dict, Any, Tuple

# ---------------------------
# Helper Functions and Utils
# ---------------------------

def show_menu() -> None:
    # """
    # Display the menu options.
    # """
    print("\nSimple Text Editor")
    print("1. Open an existing file (e.g., enter '1' to open 'myfile.txt')")
    print("2. Create a new file (e.g., enter '2' to create 'newfile.txt')")
    print("3. Search and replace (e.g., enter '3')")
    print("4. Undo last change (e.g., enter '4')")
    print("5. Redo last undone change (e.g., enter '5')")
    print("6. Exit (e.g., enter '6')")

def save_file(filename: str, content: str, mode: str = 'w') -> None:
    # """
    # Save the content to the specified file.
    # If the file exists and mode is 'w', create a backup with a timestamp.
    # """
    try:
        if os.path.exists(filename) and mode == 'w':
            backup_filename = f"{filename}.{datetime.now().strftime('%Y%m%d%H%M%S')}.bak"
            os.rename(filename, backup_filename)
            print(f"Backup created: {backup_filename}")
        with open(filename, mode) as file:
            file.write(content)
        print(f"Saved file '{filename}'.")
    except IOError as e:
        print(f"Error saving file '{filename}': {e}")

def save_history(history: List[Dict[str, str]], filename: str = "edit_history.json") -> None:
    # """
    # Save the edit history to a JSON file.
    # """
    try:
        with open(filename, 'w') as f:
            json.dump(history, f, indent=4)
        print(f"Edit history saved to {filename}.")
    except IOError as e:
        print(f"Error saving edit history: {e}")

# ---------------------------
# File Operations
# ---------------------------

def open_file() -> Tuple[str, str]:
    """
    Prompt the user to enter a filename to open. Repeats until a valid file is provided.
    Returns the filename and its content.
    """
    while True:
        filename = input("Enter the filename to open (e.g., myfile.txt): ").strip()
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                content = file.read()
            print(f"Opened file '{filename}'.")
            return filename, content
        else:
            print(f"File '{filename}' not found. Please try again.")

def create_file() -> Tuple[str, str]:
    """
    Prompt the user to create a new file. If the file exists, ask again for a new filename.
    Returns the new filename and an empty content string.
    """
    while True:
        filename = input("Enter the filename to create (e.g., newfile.txt): ").strip()
        if os.path.exists(filename):
            print(f"File '{filename}' already exists. Please choose a different name.")
        else:
            with open(filename, 'w') as file:
                pass
            print(f"Created new file '{filename}'.")
            return filename, ""

# ---------------------------
# Content Editing and Processing
# ---------------------------

def edit_content(content: str, append: bool = False) -> str:
    """
    Edit the content of the file.
    Prompts the user to input text line by line until 'SAVE' is entered.
    Example: Type your text, then type 'SAVE' on a new line to finish.
    """
    if append:
        print("Appending to the file. Enter your text (type 'SAVE' to save and exit):")
    else:
        print("Overwriting the file. Enter your text (type 'SAVE' to save and exit):")
    
    new_content = "" if not append else content
    while True:
        line = input()
        if line.strip().upper() == 'SAVE':
            break
        new_content += line + "\n"
    return new_content

def search_replace(content: str) -> str:
    """
    Search for specific words or phrases in the text and replace them with new content.
    """
    search_term = input("Enter the word or phrase to search for (e.g., 'old'): ").strip()
    replace_term = input("Enter the new word or phrase to replace with (e.g., 'new'): ").strip()
    if search_term in content:
        content = content.replace(search_term, replace_term)
        print(f"Replaced all occurrences of '{search_term}' with '{replace_term}'.")
    else:
        print(f"'{search_term}' not found in the content.")
    return content

# ---------------------------
# Undo/Redo Functionality with History
# ---------------------------

def undo_change(history: List[Dict[str, str]], redo_stack: List[Dict[str, str]]) -> str:
    """
    Undo the last change by reverting to the previous state.
    Returns the content of the previous state.
    """
    if history:
        redo_stack.append(history.pop())
        if history:
            print("Undo successful.")
            return history[-1]["content"]
        else:
            print("Nothing to undo. Reverting to empty content.")
            return ""
    else:
        print("Nothing to undo.")
        return ""

def redo_change(history: List[Dict[str, str]], redo_stack: List[Dict[str, str]]) -> str:
    """
    Redo the last undone change.
    Returns the redone content.
    """
    if redo_stack:
        change = redo_stack.pop()
        history.append(change)
        print("Redo successful.")
        return change["content"]
    else:
        print("Nothing to redo.")
        return history[-1]["content"] if history else ""

# ---------------------------
# Main Application Logic
# ---------------------------

def main() -> None:
    """
    Main function to run the Simple Text Editor application.
    """
    filename = "default.txt"  # Default filename if not set later
    edit_history: List[Dict[str, str]] = []  # List of dicts with timestamp and content
    redo_stack: List[Dict[str, str]] = []
    content: str = ""

    while True:
        show_menu()
        # Validate menu choice
        while True:
            choice = input("Enter your choice (1-6): ").strip()
            if choice in [str(i) for i in range(1, 7)]:
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6 (e.g., '1').")

        if choice == '1':
            filename, content = open_file()
            while True:
                mode = input("Do you want to overwrite (O) or append (A) the file? (e.g., O): ").strip().upper()
                if mode in ['O', 'A']:
                    break
                print("Invalid choice. Please enter 'O' for overwrite or 'A' for append (e.g., 'O').")
            if mode == 'A':
                content = edit_content(content, append=True)
                save_file(filename, content, mode='w')  # Write new content (with appended text)
            else:
                content = edit_content("", append=False)
                save_file(filename, content)
            edit_history.append({"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "content": content})
        elif choice == '2':
            filename, content = create_file()
            content = edit_content("")
            save_file(filename, content)
            edit_history.append({"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "content": content})
        elif choice == '3':
            filename, content = open_file()
            content = search_replace(content)
            save_file(filename, content)
            edit_history.append({"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "content": content})
        elif choice == '4':
            content = undo_change(edit_history, redo_stack)
        elif choice == '5':
            content = redo_change(edit_history, redo_stack)
        elif choice == '6':
            save_file(filename, content)
            # Save edit history to a JSON file upon exit
            save_history(edit_history)
            print("Exiting the Simple Text Editor. Goodbye!")
            break

if __name__ == "__main__":
    main()