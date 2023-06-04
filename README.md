# Binary File Detector

This Python script allows users to check if a given file is a binary file and, if so, detect the intended operating system for the file.

## Description

The script supports PE files (Windows), ELF files (Unix/Linux), and Mach-O files (MacOS). If a file can't be parsed as any of these, the function returns "Unknown". 

Please note, handling binaries can get complex quickly and this script provides a basic level of support. It's also important to understand that these checks may fail for malformed or unusual binary files and it doesn't account for every possible edge case.

## Getting Started

### Dependencies

* Python 3.x
* The script requires that `pefile`, `pyelftools` and `macholib` be installed.

### Installing

1. Clone the repository: 
   ```bash
   git clone https://github.com/grispan56/filer.git
```

2. Install the required dependencies:

4. Executing program
Run the script on a file:

bash
Copy code
python binary_file_detector.py /path/to/your/file
Use --help for usage information:

bash
Copy code
python binary_file_detector.py --help
