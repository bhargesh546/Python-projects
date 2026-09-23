"""
The ISBN (International Standard Book Number) is a unique identifier assigned to commercial books. 
It can be either 10 or 13 digits long, and the last digit is a check digit calculated from the other digits.

When the user runs the program, it will show the prompt Enter ISBN and length: . 
The user can enter the ISBN code they want to validate in ISBN,length format. 
The ISBN code should not contain hyphens, followed by its length (10 or 13), separated by a comma.

Example inputs: 1530051126,10 for ISBN-10 codes. 
                9781530051120,13 for ISBN-13 codes.

When we complete the project, the user should see the following messages depending on the values they enter.

| ISBN Code	| Length	| Message	| Example input |
| --- | --- | --- | --- |
| Valid	| Valid	| Valid ISBN Code.	| 1530051126,10 |
| Invalid Number	| Valid	| Invalid ISBN Code.	| 1530051125,10 |
| Does not match specified length or left blank	| Valid	| ISBN-10 code should be 10 digits long. or ISBN-13 code should be 13 digits long., depending on the length they entered.	| 9781530051120,10 or 1530051126,13 |
| Contains non-numeric characters (except for the check digit)	| Valid	| Invalid character was found.	| 15-0051126,10 |
| Any	| Invalid Number	| Length should be 10 or 13.	| 1530051126,9 |
| Any	| Contains non-numeric characters or left blank	| Length must be a number.	| 1530051125,A |
| Not comma-separated	 | Not comma-separated	| Enter comma-separated values.	| 1530051125 |

"""
def main():
    user_input = input('Enter ISBN and length: ')
    try:
        values = user_input.split(',')
        isbn = values[0]
        length = int(values[1])
    except IndexError:
        print("Enter comma-separated values.")
        return
    except ValueError:
        print("Length must be a number.")
        return

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')

def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    
    main_digits = isbn[0:length-1]
    if not main_digits.isdecimal():
        print("Invalid character was found.")
        return

    given_check_digit = isbn[length-1]
    main_digits_list = [int(digit) for digit in main_digits]
    
    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def calculate_check_digit_10(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    
    # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    
    # Find the remainder of dividing the sum by 11, then subtract it from 11
    result = 11 - digits_sum % 11
    
    # The calculation result can range from 1 to 11.
    # If the result is 11, use 0.
    # If the result is 10, use upper case X.
    # Use the value as it is for other numbers.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def calculate_check_digit_13(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    
    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    
    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10
    
    # The calculation result can range from 1 to 10.
    # If the result is 10, use 0.
    # Use the value as it is for other numbers.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


if __name__ == "__main__":
    main()
