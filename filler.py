"""Binary File Detector.

This script allows the user to check if a given file is a binary file and if so,
detect the intended OS for the file.

This script requires that `pefile`, `pyelftools` and `macholib` be installed within the Python
environment you are running this script on.

This file can also be imported as a module and contains the following functions:

    * is_binary - returns whether a file is binary
    * detect_os - returns the OS the binary file is intended for
    * main - the main function of the script
"""

import argparse
import pefile
from elftools.elf.elffile import ELFFile
from macholib.MachO import MachO

def is_binary(file):
    """Check if file is binary.

    Args:
        file (str): The file to be checked.

    Returns:
        bool: The return value. True for binary, False otherwise.
    """
    try:
        with open(file, 'rb') as f:
            return b'\0' in f.read()
    except Exception as e:
        print(f"Error while checking if file is binary: {e}")
        return False

def detect_os(file):
    """Detect the OS of a binary file.

    Args:
        file (str): The binary file to be checked.

    Returns:
        str: The detected OS. Can be 'Windows', 'Unix/Linux', 'MacOS' or 'Unknown'.
    """
    try:
        pe = pefile.PE(file)
        return "Windows"
    except pefile.PEFormatError as e:
        print(f"PE file error: {e}")

    try:
        with open(file, 'rb') as f:
            elffile = ELFFile(f)
            return "Unix/Linux"
    except Exception as e:  # ELF parsing can fail for several reasons
        print(f"ELF file error: {e}")

    try:
        macho = MachO(file)
        return "MacOS"
    except ValueError as e:  # macholib throws ValueError on non-Mach-O files
        print(f"Mach-O file error: {e}")

    return "Unknown"

def main():
    parser = argparse.ArgumentParser(description='Detect OS of a binary file.')
    parser.add_argument('file', help='The file to check')
    args = parser.parse_args()

    file = args.file

    if is_binary(file):
        print("This is a binary file.")
        print("Intended OS: " + detect_os(file))
    else:
        print("This is not a binary file.")

if __name__ == "__main__":
    main()
