from advent_2020.helpers import get_input


if __name__ == "__main__":
    adapters = [0] + sorted(map(int, get_input()))
    n1, n3 = 0, 1
    for a, b in zip(adapters[:-1], adapters[1:]):
        n1 += b - a == 1
        n3 += b - a == 3
    print(n1 * n3)
