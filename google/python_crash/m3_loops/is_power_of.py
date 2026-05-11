
def main():
    number_p = float(input("enter the number: "))
    base_n = float(input("Enter the base: "))
    is_power = is_power_of(number_p, base_n)
    if is_power:
        print(f"{is_power}, {number_p} is a power of {base_n}")
    else:
        print(f"{is_power}, {number_p} is not a power of {base_n}")


def is_power_of(number, base):
    if number < base:           # Base case: when number is smaller than base.
        return number == 1
    
    # Recursive case: keep dividing number by base.
    return is_power_of(number/base, base)

if __name__ == "__main__":
    main()