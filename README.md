# CommandCrafter

CommandCrafter is a powerful Command Line Interface (CLI) tool designed to streamline file management tasks and enhance productivity.

## Installation

1. Clone the repository: git clone https://github.com/divyesh123-jain/CommandCrafter.git
2. Navigate to the project directory:

## Usage

1. Make sure you have Python installed on your system.
2. Navigate to the project directory.
3. Run the CLI tool with the following command:
python main.py [command] [arguments]



### Available Commands:

- **create**: Create a new file with optional content.
python main.py create filename.txt -c "Content of the file"


- **delete**: Delete an existing file.
python main.py delete filename.txt


- **copy**: Copy a file to another location.
python main.py copy source_file.txt destination_directory/


- **move**: Move a file to another location.
python main.py move source_file.txt destination_directory/


- **list**: List all files in a directory.
python main.py list [directory]


- **drives**: List all available drives.
python main.py drives


- **open-file**: Open a file with the default application.
python main.py open-file filename.txt


- **open-folder**: Open a folder with the default file manager.
python main.py open-folder directory/


- **cpu**: Check CPU usage.
python main.py cpu


## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
