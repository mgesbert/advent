from advent_2020.helpers import get_input


if __name__ == "__main__":
    data = list(get_input())
    counter = 0
    for line in data:
        head, password = line.split(": ")
        head, c = head.split(" ")
        low, high = map(int, head.split("-"))
        counter += (password[low - 1] == c) != (password[high - 1] == c)
    print(counter)
