from advent_2020.helpers import get_input


if __name__ == "__main__":
    data = list(map(int, get_input()))

    for i, x in enumerate(data):
        for j, y in enumerate(data):
            for k, z in enumerate(data):
                if i == j or i == k or j == k:
                    continue
                if x + y + z != 2020:
                    continue
                print(x * y * z)
                exit(0)
