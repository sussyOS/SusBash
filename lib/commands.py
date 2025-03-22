import os
import sys

def run_command(command):
    match command:
        case "exit":
            sys.exit(0)
        case "help":
            print("""
                  exit - exit the shell
                  help - show this message
                  cls - clear the screen
                  cd - change directory
                  ls - list files in current directory
                  """)
        case "cls":
            if sys.platform == "win32":
                os.system("cls")
            else:
                os.system("clear")
        case _:
            command = command.split()
            if command[0] == "cd":
                try:
                    os.chdir(command[1])
                except FileNotFoundError:
                    print(f"Directory not found: {command[1]}")
            elif command[0] == "ls":
                print("\n".join(os.listdir()))
            else:
                print(f"Command not found: {command}")