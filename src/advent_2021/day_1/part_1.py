from advent_2021.helpers import get_input


if __name__ == "__main__":
    data = list(map(int, get_input()))
    print(sum(a < b for a, b in zip(data[:-1], data[1:])))
