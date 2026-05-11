
def main():
    while True:
        try:
            sec = int(input("Enter seconds to be converted: "))
            break
        except ValueError:
            continue

    hours, minutes, seconds = convert_seconds(sec)
    print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
 
if __name__ == "__main__":
    main()