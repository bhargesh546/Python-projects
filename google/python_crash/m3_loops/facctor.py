# This function counts the number of integer factors for a "given_number" variable, 
# passed through the function’s parameters.
# The "count" return value includes the "given_number" itself as a 
# factor (n*1). 

def main():
    number = int(input("Enter the number whose factor is to calculated: "))
    factor_count, factors = count_factors(number)
    print(f"There are {factor_count} factors of {number}: {factors}")

def count_factors(given_number):

    # To include the "given_number" variable as a "factor", initialize
    # the "factor" variable with the value 1 (if the "factor" variable
    # were to start at 2, the "given_number" itself would be excluded). 
    
    factor = 1
    count = 1
    
    factor_list = []

    # This "if" block will run if the "given_number" equals 0.
    
    if given_number == 0:
        # If True, the return value will be 0 factors. 
        return 0

    # The while loop will run while the "factor" is still less than
    # the "given_number" variable.
    
    while factor < given_number:

        if given_number % factor == 0:
            factor_list.append(factor)
            # If True, then the "factor" variable is added to the count of
            # the "given_number"’s integer factors.
            count += 1

        factor += 1

    factor_list.append(given_number)
    # When the interpreter exits either the while loop or the top if
    # block, it will return the value of the "count" variable.
    return count, factor_list



if __name__ == "__main__":
    main()

"""    
print(count_factors(0)) # Count value should be 0
print(count_factors(3)) # Should count 2 factors (1x3)
print(count_factors(10)) # Should count 4 factors (1x10, 2x5)
print(count_factors(24)) # Should count 8 factors (1x24, 2x12, 3x8, and 4x6).

"""