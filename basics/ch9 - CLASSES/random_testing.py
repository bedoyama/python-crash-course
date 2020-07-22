from random import randint, choice


def print_distribution(total=100, x=10):
    """generates (total) numbers between 1 and (x) and prints distribution"""

    hist_data = [0 for idx in range(x)]
    average = int(total / x)

    print(hist_data)

    for idx in range(total):
        hist_data[randint(1, x) - 1] += 1

    print(hist_data)
    print(f"checksum({sum(hist_data)})")

    counter = ""

    for idy in range(average):
        counter = counter + '+'

    print(f"--: {counter}")

    for idx in range(len(hist_data)):
        counter = ""

        for idy in range(hist_data[idx]):
            counter = counter + 'o'

        print(f"{idx:02}: {counter}")


def select_players():
    players = ['rolo', 'rooshv', 'mario', 'arielle', 'jenna']

    for ids in range(10):
        print(choice(players))

print_distribution(2400, 20)
