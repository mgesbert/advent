from advent_2020.helpers import get_input

if __name__ == "__main__":
    data = list(map(int, get_input()))

    for i, x in enumerate(data):
        for j, y in enumerate(data):
            if i == j:
                continue
            if x + y != 2020:
                continue
            print(x * y)
            exit(0)
