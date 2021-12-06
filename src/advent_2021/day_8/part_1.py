from advent_2021.helpers import get_input


if __name__ == "__main__":
    print(
        sum(
            len(digit) in [2, 3, 4, 7]
            for line in get_input()
            for digit in line.split(" | ")[1].split()
        )
    )
