import os
import sys

"""For Colorized : Comment out line 6-8, 165-168 & comment in line 160-162
"""
# import colorama
# from colorama import Fore, Back, Style
# colorama.init(autoreset=True)



# List to store recorded commands
command_history = []


# "map" command (pwd)
def map():
    current_dir = os.getcwd()
    print(current_dir)


# "inventory" command (ls)
def inventory():
    files = os.listdir(".")
    for file in files:
        print(file)


# "today" command (date)
def today():
    os.system("date")


# "fork" system call
def fork():
    return os.fork()


# "execvp" system call
def execvp(command, args):
    try:
        args = command.split()
        os.execvp(args[0], args)
    except ValueError:
        print("Invalid command:", command)
        sys.exit(1)


# "pipe" system call
def pipe():
    return os.pipe()


# "open" system call
def open_file(file_path, mode):
    return os.open(file_path, mode)


# "read" system call
def read(fd, count):
    return os.read(fd, count)


# "write" system call
def write(fd, data):
    return os.write(fd, data)


# "chdir" system call
def chdir(directory):
    os.chdir(directory)


# "go" command (cd)
def go(directory):
    try:
        chdir(os.path.join(os.getcwd(), directory))
        print("Current directory changed to '{}'".format(os.getcwd()))
    except FileNotFoundError:
        print("Directory '{}' not found.".format(directory))
    except NotADirectoryError:
        print("'{}' is not a directory.".format(directory))
    except PermissionError:
        print("Permission denied: Unable to change directory to '{}'.".format(directory))
    except Exception as e:
        print("An error occurred while changing directory to '{}': {}".format(directory, str(e)))


# "back" command (cd ..)
def back():
    try:
        parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
        chdir(parent_dir)
        print("Navigated to the previous directory: '{}'".format(os.getcwd()))
    except FileNotFoundError:
        print("Previous directory not found.")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print("Error: {}".format(str(e)))


# "make" command (mkdir)
def make(directory):
    try:
        os.mkdir(directory)
        print("Directory '{}' created successfully.".format(directory))
    except FileExistsError:
        print("Directory '{}' already exists.".format(directory))
    except PermissionError:
        print("Permission denied '{}'.".format(directory))
    except Exception as e:
        print("Error creating directory '{}': {}".format(directory, str(e)))


# "feel" command (touch)
def feel(filename):
    try:
        with open(filename, "a") as file:
            text = input("Enter text to append to the file: ")
            file.write(text + "\n")
        print("Text appended to the file '{}' successfully.".format(filename))
    except Exception as e:
        print("An error occurred while appending text to the file '{}': {}".format(filename, str(e)))


# "ink" command (echo)
def ink(message):
    print(message)


# "sweep" command (cls)
def sweep():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


# "record" command (history)
def record():
    for index, command in enumerate(command_history, start=1):
        print(f"{index}: {command}")


# "vanish" command (rm)
def vanish(filename):
    try:
        os.unlink(filename)
        print("File '{}' removed successfully.".format(filename))
    except FileNotFoundError:
        print("File '{}' not found.".format(filename))
    except PermissionError:
        print("Permission denied: Unable to remove file '{}'.".format(filename))
    except Exception as e:
        print("Error removing file '{}': {}".format(filename, str(e)))


# Greetings
def printGreeting():
    print("Welcome to Turtle Shell")
    print("Say Cheese")

#Greetings Colorized
# def printGreeting():
#     print(Fore.CYAN+"Welcome to Turtle Shell")
#     print(Fore.GREEN + "Say Cheese")
#     print(Style.RESET_ALL)

    

# Main Function
def main():
    printGreeting()

    while True:
        command = input("\n>> ")

        # Add entered command to the command_history list
        command_history.append(command)

        if command == "map":
            map()
        elif command == "inventory":
            inventory()
        elif command == "today":
            today()
        elif command == "quit":
            break
        elif command.startswith("go "):
            directory = command[3:].strip()
            go(directory)
        elif command == "back":
            back()
        elif command.startswith("make "):
            directory = command[5:].strip()
            make(directory)
        elif command.startswith("feel "):
            filename = command[5:].strip()
            feel(filename)
        elif command.startswith("ink "):
            message = command[4:].strip()
            ink(message)
        elif command == "sweep":
            sweep()
        elif command == "record":
            record()
        elif command.startswith("vanish "):
            filename = command[7:].strip()
            vanish(filename)
        else:
            # Unknown command: execute using execvp
            pid = fork()
            if pid == 0:
                execvp(command, [])
                sys.exit("Command execution failed")
            else:
                os.waitpid(pid, 0)


if __name__ == "__main__":
    main()
