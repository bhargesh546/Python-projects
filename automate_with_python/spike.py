import time, sys

def main():
    increasing_len = int(input("Enter the highest length: ")) + 1
    spike(increasing_len)

def spike(len):
    try:
        while True:  # The main program loop
            # Draw lines with increasing length:
            for i in range(1, len):
                print('-' * (i * i))
                time.sleep(0.1)

            # Draw lines with decreasing length:
            for i in range(len - 1, 1, -1):
                print('-' * (i * i))
                time.sleep(0.1)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()