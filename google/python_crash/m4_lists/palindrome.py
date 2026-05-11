"""
This function accepts a given string and checks each character of the string to see 
if it is a letter or not.

A palindrome is a word, phrase, number, or sequence of characters that reads the 
same forward and backward (ignoring spaces, punctuation, and capitalization).
"""
def main():
    text_string = input("Enter the text for palindrome check: ")
    print(palindrome(text_string))

def mirrored_string(my_string):

    # Two variables are initialized as string data types using empty 
    # quotes. The variable "forwards" will hold the "my_string"
    # minus any character that is not a letter. The "backwards" 
    # variable will hold the same letters as "forwards", but in  
    # in reverse order.

    forwards = ""
    backwards = ""

    # The for loop iterates through each character of the "my_string"
    for character in my_string:

        # The if-statement checks if the character is not a space.
        if character.isalpha():
            forwards += character
            backwards = character + backwards

        # If False (meaning the character is not a letter), no action is needed. 
        
    # The final if-statement compares the "forwards" and "backwards"
    # strings to see if the letters are the same both forwards and
    # backwards. Since Python is case sensitive, the two strings will 
    # need to be converted to use the same case for this comparison. 
    
    if forwards.lower() == backwards.lower():
        return True
    return False
 
def palindrome(text):
    cleaned = "".join([char.lower() for char in text if char.isalpha()])

    if cleaned == cleaned[::-1]:
        return f"The text is palindrome {text} = {cleaned[::-1]}"

#print(mirrored_string("12 Noon")) # Should be True
#print(mirrored_string("Was it a car or cat I saw")) # Should be False
#print(mirrored_string("'eve, Madam Eve")) # Should be True

if __name__ == "__main__":
    main()