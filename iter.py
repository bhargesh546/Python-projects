temp = [221, 234, 256, 345, 159, 900]

new_temp = [i / 10 if i != 900 else 0 for i in temp]

# new_temp = list(map(lambda x: x/10, temp))

print(new_temp)