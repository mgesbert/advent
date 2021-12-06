from advent_2021.helpers import get_input


if __name__ == "__main__":
    data = list(map(int, get_input()))
    print(
        sum(
            sum(data[i : i + 3]) < sum(data[i + 1 : i + 4])
            for i in range(len(data) - 3)
        )
    )
