## INET 4031 Add User Script (Python)

### Description

This Python script is designed to streamline the process of adding users and groups to a system. It reads user/group data from an input file, processes the file line-by-line, and adds each user to the system. Below, we explain key components of the code:

- **Imports:** The script uses several Python modules for different functionalities. For example:
  - `os`: It provides access to operating system functions and is used to execute system commands.
  - `re`: This module is used for regular expressions. In this script, it helps identify lines starting with a `#` character and other pattern matching.
  - `sys`: This module provides access to system-specific parameters and functions. It's used to read input from the standard input (stdin).

- **Regular Expression (`re`):** The regular expression is used to check for the presence of a `#` at the start of each line in the input file. Lines starting with `#` are skipped during processing.

- **Input File Format:** The input file is expected to follow this format:
### Operation

#### Input File Specification

1. **Input File Format:** The input file should adhere to the specified format, which consists of colon-separated fields for user information. Each line in the input file should have the following structure:

username:default_password:last_name:first_name:comma_separated_list_of_groups


2. **Input File Name:** While you can choose the name of the input file, a common convention is to name it `create-users.input`.

#### Running the Script

1. **Python Version:** Ensure that you have Python installed on your system. This script is compatible with Python 2.

2. **Permissions:** Make sure you have read permissions for the input file to read data from it and execution permissions on the Python script.

3. **Execution Command:** To run the script, open your terminal and execute the following command:

```bash
python3 create_users.py < create_users.input


