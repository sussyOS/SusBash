import os
import sys

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
                else:
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