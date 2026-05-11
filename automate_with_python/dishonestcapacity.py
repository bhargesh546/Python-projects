"""
A program to calculate how misleading hard drive and flash memory manufacturers
are while advertising their product capacities.
"""

def main():
    unit = input('Enter TB or GB for the advertised unit: ')
    advertised_capacity = float(input('Enter the advertised capacity:'))
    real_capacity = capacity(advertised_capacity, unit)
    print(f"The actual capacity is {real_capacity} unit")


def capacity(capacity, unit):

    # Calculate the amount that the advertised capacity lies:
    if unit == 'TB' or unit == 'tb':
        discrepancy = 1000000000000 / 1099511627776     # 1tb = 1024^4 = 1099511627776 bytes
    elif unit == 'GB' or unit == 'gb':
        discrepancy = 1000000000 / 1073741824           # 1gb = 1024^3 = 1073741824 bytes

    return round(capacity * discrepancy, 2)

if __name__ == "__main__":
    main()