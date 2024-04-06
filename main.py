import argparse
import os
import shutil
import sys
import psutil
import subprocess


def create_file(filename, content=None):
    """Create a new file with optional content."""
    try:
        with open(filename, 'w') as f:
            if content:
                f.write(content)
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating file '{filename}': {e}")


def delete_file(filename):
    """Delete an existing file."""
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
    except Exception as e:
        print(f"Error deleting file '{filename}': {e}")


def copy_file(source, destination):
    """Copy a file from source to destination."""
    try:
        shutil.copyfile(source, destination)
        print(f"File '{source}' copied to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"Error: '{source}' not found.")
    except Exception as e:
        print(f"Error copying file '{source}' to '{destination}': {e}")


def move_file(source, destination):
    """Move a file from source to destination."""
    try:
        shutil.move(source, destination)
        print(f"File '{source}' moved to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"Error: '{source}' not found.")
    except Exception as e:
        print(f"Error moving file '{source}' to '{destination}': {e}")


def list_files(directory):
    """List all files in a directory."""
    try:
        files = os.listdir(directory)
        print(f"Files in '{directory}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except Exception as e:
        print(f"Error listing files in directory '{directory}': {e}")


def list_drives():
    """List all available drives."""
    drives = []
    if sys.platform.startswith('win'):
        drives = ['%s:\\' % d for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists('%s:' % d)]
    else:
        drives = [os.path.join('/media', d) for d in os.listdir('/media') if os.path.isdir(os.path.join('/media', d))]
    print("Available drives:")
    for drive in drives:
        print(drive)


def open_file(filename):
    """Open a file using the default application."""
    try:
        if sys.platform.startswith('darwin'):  # macOS
            subprocess.call(('open', filename))
        elif os.name == 'nt':  # Windows
            os.startfile(filename)
        elif os.name == 'posix':  # Linux, Unix
            subprocess.call(('xdg-open', filename))
        print(f"Opened '{filename}' with the default application.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")


def open_folder(folder):
    """Open a folder using the default file manager."""
    try:
        if sys.platform.startswith('darwin'):  # macOS
            subprocess.call(('open', folder))
        elif os.name == 'nt':  # Windows
            subprocess.Popen(['explorer', folder])
        elif os.name == 'posix':  # Linux, Unix
            subprocess.Popen(['xdg-open', folder])
        print(f"Opened folder '{folder}' with the default file manager.")
    except Exception as e:
        print(f"Error opening folder '{folder}': {e}")


def check_cpu_usage():
    """Check CPU usage."""
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")
    except Exception as e:
        print(f"Error checking CPU usage: {e}")


def main():
    parser = argparse.ArgumentParser(description="Advanced File Management CLI Tool")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create sub-command
    create_parser = subparsers.add_parser("create", help="Create a new file")
    create_parser.add_argument("filename", help="Name of the file to create")
    create_parser.add_argument("-c", "--content", help="Content to write to the file")

    # Delete sub-command
    delete_parser = subparsers.add_parser("delete", help="Delete an existing file")
    delete_parser.add_argument("filename", help="Name of the file to delete")

    # Copy sub-command
    copy_parser = subparsers.add_parser("copy", help="Copy a file")
    copy_parser.add_argument("source", help="Source file to copy")
    copy_parser.add_argument("destination", help="Destination to copy the file")

    # Move sub-command
    move_parser = subparsers.add_parser("move", help="Move a file")
    move_parser.add_argument("source", help="Source file to move")
    move_parser.add_argument("destination", help="Destination to move the file")

    # List sub-command
    list_parser = subparsers.add_parser("list", help="List all files in a directory")
    list_parser.add_argument("directory", nargs="?", default=".", help="Directory to list files (default: current directory)")

    # List drives sub-command
    drives_parser = subparsers.add_parser("drives", help="List all available drives")

    # Open file sub-command
    open_file_parser = subparsers.add_parser("open-file", help="Open a file")
    open_file_parser.add_argument("filename", help="Name of the file to open")

    # Open folder sub-command
    open_folder_parser = subparsers.add_parser("open-folder", help="Open a folder")
    open_folder_parser.add_argument("folder", help="Name of the folder to open")

    # Check CPU usage sub-command
    cpu_parser = subparsers.add_parser("cpu", help="Check CPU usage")

    args = parser.parse_args()

    if not args.command:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.command == "create":
        create_file(args.filename, args.content)
    elif args.command == "delete":
        delete_file(args.filename)
    elif args.command == "copy":
        copy_file(args.source, args.destination)
    elif args.command == "move":
        move_file(args.source, args.destination)
    elif args.command == "list":
        list_files(args.directory)
    elif args.command == "drives":
        list_drives()
    elif args.command == "open-file":
        open_file(args.filename)
    elif args.command == "open-folder":
        open_folder(args.folder)
    elif args.command == "cpu":
        check_cpu_usage()


if __name__ == "__main__":
    main()
