def change_string(given_string):
    words = given_string.split(" ")

    new_string = ""

    for word in words:
        new_string += word[1:] + "-" + word[0] + " "
    
    return new_string.strip()

print(change_string("1one 2two 3three 4four 5five"))