with open("vegetables.txt", "x+") as file:
    file.write("Tomato\nGinger\nOnion")
    file.seek(0)
    content = file.read()

print(content)