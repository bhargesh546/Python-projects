# This function converts fluid ounces to milliliters and returns the 
# result of the conversion.

def main():
    while True:
        try:
            ounce = float(input("Enter the ounce value: "))
            break
        except ValueError:
            continue
    
    ml = convert_volume(ounce)
    print(f"{ounce} ounce in ml is: {ml}")

def convert_volume(fluid_ounce):
# Calculate value of the "ml" variable using the parameter variable 
# "fluid_ounce". There are approximately 29.5 milliliters in 1 fluid
# ounce.
    ml = fluid_ounce * 29.5  
# Return the result of the calculation.  
    return ml

if __name__ == "__main__":
    main()
    