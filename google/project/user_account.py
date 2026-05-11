import csv                  # This library helps read and write the CSV files. 
import secrets              # This helps generate random passwords for each user account. 
import subprocess           # This calls the useradd command, which creates and adds each user account.
from pathlib import Path    # This library helps to locate the data files for each user account.

cwd = Path.cwd()

with open(cwd / "data/users_in.csv", "r") as file_input, open(cwd / "data/users_out.csv", "a") as file_output:
    reader = csv.DictReader(file_input)
    writer = csv.DictWriter("file_output", fieldnames= reader.fieldnames)

    for row in reader:
        row["password"] = secrets.token_hex(8)
        useradd_cmd = [
            "/sbin/useradd",                # Linux command to create a new user
            "-c", row["real_name"],         # adds a comment (usually full name)
            "-m",                           # creates a home directory
            "-G", "users",                  # adds user to "users" group
            "-p", row["password"],          # sets password (usually encrypted)
            row["username"]                 # the username
        ]
        subprocess.run(useradd_cmd, check=True)

        writer.writerow(row)