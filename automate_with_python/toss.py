import random, logging

logging.basicConfig(filename="tossLog.txt", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.debug("Start of the program")

guess = ''
while guess not in ('heads', 'tails'):
    guess = input('Guess the coin toss! Enter heads or tails: ').lower()

logging.debug(f"value of guess: {guess}")

toss = random.choice(["heads", "tails"])  # 0 is tails, 1 is heads

logging.debug(f"Value of toss: {toss}")

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input('Guess the coin toss! Enter heads or tails: ').lower()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug("End of the toss program.")
logging.debug(f"{"-"*20}")