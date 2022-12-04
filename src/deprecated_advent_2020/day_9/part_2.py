import sys

from advent_2020.helpers import get_input


if __name__ == "__main__":
    values = list(map(int, get_input()))
    invalid_number = 248131121
    for i in range(len(values) - 1):
        j = i + 1
        acc = values[i] + values[j]
        while acc < invalid_number:
            j += 1
            acc += values[j]
        if acc == invalid_number:
            print(min(values[i : j + 1]) + max(values[i : j + 1]))
            sys.exit(0)
