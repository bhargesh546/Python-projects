import logging

logging.basicConfig(filename="factorialLog.txt", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.debug("Start of the program")

def main():
    num = int(input("Enter a number to calculate the factorial: "))
    print(factorial(num))

def factorial(n):
    logging.debug(f"Start of factorial {n}")
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug(f"i is {i}, total is {total}")

    logging.debug("End of the factorial({n}) program")
    return f"The factorial of {n} is {total}."

if __name__ == "__main__":
    main()


