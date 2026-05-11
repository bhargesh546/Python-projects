import sys      # to check for builtin modules using `sys.builtin_module_names`
import time, os

while True:
    if os.path.exists("./vegetables.txt"):
        with open("./vegetables.txt") as file:
            print(file.read())
    else:
        print("File does not exists.")
    time.sleep(5)