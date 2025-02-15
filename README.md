# Text_Editor

## Overview

**Text_Editor** is a simple text editor application built in Python. This repository contains two versions of the code:

- **Original Version:** The basic implementation that provides core functionalities such as opening, creating, editing, searching & replacing, and saving text files.
- **Enhanced Version:** An improved version with robust input validation, clearer instructions (including example inputs), enhanced error handling, and additional features like backup creation and edit history saving.

Both versions are designed to be easy to follow and user-friendly, ensuring that even with invalid inputs, the user is guided to provide correct data.

## Features

- **Menu-Driven Interface:** Easy-to-use command-line menu for navigating options.
- **File Operations:** Open, create, and save text files with clear prompts.
- **Content Editing:** Supports both overwriting and appending text. Type 'SAVE' to finish editing.
- **Search and Replace:** Find and replace words or phrases within a file.
- **Undo/Redo Functionality:** Supports reverting to previous states using an edit history (enhanced version).
- **Backup Creation:** Automatically creates a timestamped backup before overwriting a file (enhanced version).
- **Edit History Persistence:** Saves a history of edits to a JSON file for reference (enhanced version).

## Installation

### Prerequisites

- Python 3.6 or higher.
- (Optional) A virtual environment for dependency isolation.

### Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/Text_Editor.git
   cd Text_Editor
   ```

2. **Create and Activate a Virtual Environment (recommended):**
   ```bash
   python -m venv venv
   # For Windows:
   venv\Scripts\activate
   # For macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   This project uses only standard Python libraries (`os`, `json`, `datetime`) plus `typing` which is included by default. No external packages are required.

## Usage

There are two versions of the text editor available:

### Original Version
- **File Name:** `original_text_editor.py`
- **How to Run:**
  ```bash
  python original_text_editor.py
  ```

### Enhanced Version
- **File Name:** `enhanced_text_editor.py`
- **How to Run:**
  ```bash
  python enhanced_text_editor.py
  ```

### General Instructions

- **Menu Options:** The application displays a menu with options. Enter the number corresponding to the action you wish to perform.
- **Input Examples:** The prompts include example inputs (e.g., "Enter the filename to open (e.g., myfile.txt)").
- **Editing Mode:** When editing content, type your text line by line. Type `SAVE` on a new line to finish editing.
- **Undo/Redo:** The enhanced version supports undo and redo functionality. Choose the appropriate menu option to revert or reapply changes.

## Code Explanation

- **File Operations:**  
  Functions like `open_file()` and `create_file()` handle file operations. They repeatedly prompt the user until valid input is provided, ensuring a smooth experience.

- **Content Editing:**  
  The `edit_content()` function collects text input until the user types `SAVE`, making it clear when to stop.

- **Search and Replace:**  
  The `search_replace()` function allows users to find a specific term and replace it with a new one, with clear feedback if the term isn’t found.

- **Undo/Redo with History (Enhanced Version):**  
  Enhanced functionality maintains an edit history and supports undo/redo operations. Additionally, a backup is created before saving changes to protect data.

- **Error Handling:**  
  Enhanced error handling throughout ensures that invalid inputs are caught, and clear, informative messages are shown to the user.

## Contributing

Contributions, bug reports, and feature requests are welcome! Please fork the repository and create a pull request with your changes. For any issues, feel free to open an issue in the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Python community for valuable resources and best practices.
- Special thanks to contributors and open-source libraries that helped shape this project.

Happy editing!
```
