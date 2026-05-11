

def main():
    while True:
        try:
            number = int(input("Enter a number: \n"))
            if number > 0:
                break
        except ValueError:
            print("Enter a valid positive integer greater than 1.")
    
    while number != 1:
        print(number, end=" ")
        number = collatz(number)
    print(number)
        

def collatz(n):
    if n % 2 == 0:
        n = n // 2
    else:
        n = (3*n) + 1
        
    return n

if __name__ == "__main__":
    main()