import os
import sys
from lib import sys as lib

path = os.path.dirname(os.path.abspath(__file__))

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
                  mkdir - create a directory
                  rm - remove a file
                  """)
        case "cls":
            os.system("cls||clear")         
        case _:
            command = command.split()
            try:
                if command[0] == "cd":
                    try:
                        os.chdir(command[1])                  
                    except FileNotFoundError:
                        print(f"Directory not found: {command[1]}")
                elif command[0] == "ls":
                    print("\n".join(os.listdir()))
                elif command[0] == "cat":
                    try:
                        with open(command[1], "r") as file:
                            print(file.read())
                    except FileNotFoundError:
                        print(f"File not found: {command[1]}")
                elif command[0] == "echo":  
                    print(" ".join(command[1:]))
                elif command[0] == "mkdir": 
                    try:
                        os.mkdir(command[1])
                    except FileExistsError:
                        print(f"Directory already exists: {command[1]}")
                elif command[0] == "rm":
                    lib.rm(command)    
                else:
                    try:
                        os.system(command[0])
                    except Exception:
                        print(f"Command not found: {command[0]}")
            except IndexError:
                print(f"Command not found: {command[0]}")
    return os.getcwd()
def main(path):
    command = input(f"{path}$: ")
    path = run_command(command)
    main(path)
if __name__ == "__main__":
    main(path)