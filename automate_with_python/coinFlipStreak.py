import random

# streak_count = 0
streak_6 = []

for experiment_number in range(1000):

    # Code that creates a list of 100 'heads' or 'tails' values

    coin_flips = []
    streak_total = 0

    for _ in range(100):
        coin_flips.append(random.choice(["H", "T"]))

    # Code that checks if there is a streak of 6 heads or tails in a row

    streaks = 1

    for i in range(1, len(coin_flips)):
        if coin_flips[i] == coin_flips[i - 1]:
            streaks += 1
        else:
            streaks = 1

        if streaks == 6:
            # streak_count += 1
            streak_total += 1

    streak_6.append(streak_total)


print(f"Chance of streak: {sum(streak_6)/len(streak_6)}")