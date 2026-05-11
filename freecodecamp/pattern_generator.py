def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    elif n <= 0:
        return "Argument must be an integer greater than 0."
    
    numbers = []

    for i in range(n):
        numbers.append(str(i+1)) 

    return " ".join(numbers)    

print(number_pattern(3))