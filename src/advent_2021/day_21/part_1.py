import sys

from advent_2021.helpers import get_input


def get_die():
    n = 0
    while True:
        yield n % 100 + 1
        n += 1


if __name__ == "__main__":
    input_getter = get_input()
    players = [
        int(next(input_getter).split(": ")[1]),
        int(next(input_getter).split(": ")[1]),
    ]
    scores = [0, 0]
    die = get_die()
    nb_rolls = 0

    while True:
        for i in range(2):
            players[i] = (players[i] + next(die) + next(die) + next(die) - 1) % 10 + 1
            scores[i] += players[i]
            nb_rolls += 3
            if scores[i] > 999:
                print(scores[1 - i] * nb_rolls)
                sys.exit()
