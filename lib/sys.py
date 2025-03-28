import os
import sys

def rm(command):
    """Remove a file or directory."""
    try:
        os.remove(command[1])
    except FileNotFoundError:
        if command[1] == "-r": 
            os.rmdir(command[2])
        elif command[1] == "-h" or command[1] == "--help":
            print("Usage: rm [options] [file]")
            print("Options:")
            print("  -r  Remove a directory and its contents")
            print("  -h, --help  Show this help message")
        else:
            print(f"File not found: {command[1]}")