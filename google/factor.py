def count_factors(number):
    factor = 1
    factors = []
    
    if number != 0:
        factors = [number]
    count = 1

    if number == 0:
        return 0

    while factor < number:
        if number % factor == 0:
            count += 1
            factors.append(factor)
        factor += 1

    return f"There are {count} factors of {number}: {factors} "

print(count_factors(2))
print(count_factors(10))