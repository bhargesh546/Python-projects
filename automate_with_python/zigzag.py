import sys, time
def main():
    indent = int(input("How many spaces to indent: "))
    zigzag(indent)

def zigzag(n):
    indent_increasing = True  # Whether the indentation is increasing or not
    try:
        while True:  # The main program loop
            print(' ' * n, end='')
            print('********')
            time.sleep(0.1) # Pause for 1/10th of a second.

            if indent_increasing:
                # Increase the number of spaces:
                n += 1
                if n == 20:
                    # Change direction:
                    indent_increasing = False
            else:
                # Decrease the number of spaces:
                n -= 1
                if n == 0:
                    # Change direction:
                    indent_increasing = True
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()