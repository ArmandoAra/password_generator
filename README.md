# Password Generator Application

This project is a simple desktop application for generating secure passwords. It is developed using Python and `Tkinter` for the graphical user interface. The application allows users to create customized passwords, copy them to the clipboard, and save them to a file for future reference.

## Features

- **Custom Password Generation**: Users can specify the number of numbers, letters, and symbols in their password.
- **Clipboard Support**: Copy the generated password to the clipboard with a single click.
- **File Saving**: Save generated passwords along with an optional service name and timestamp to a selected file or create a new file.
- **File Selection**: Choose an existing file to save passwords using a file dialog.
- **Responsive Buttons**: Buttons change color when hovered over for improved user experience.

## Installation

1. Ensure you have Python 3 installed on your system.
2. Clone or download this repository.
3. Install dependencies
4. Place the logic.py file (containing the pass_gen function) in the same directory as the main script.

Usage
Run the application:

python main.py
Input the desired quantity of numbers, letters, and symbols for your password.

Optionally, specify a service name for the password (e.g., "Email").

Click Generate to create a password.

Use the Copy button to copy the password to your clipboard.

Use the Save button to save the password to a file:

If no file is selected, a new file will be created in the saved folder.
If a file is selected, the password will be appended to it.

project/
│
├── main.py # Main application script
├── logic.py # Contains the pass_gen function for password generation
└── saved/ # Folder to store saved password files (created dynamically)

License
This project is developed for educational purposes and is free to use. Feel free to modify and distribute.
