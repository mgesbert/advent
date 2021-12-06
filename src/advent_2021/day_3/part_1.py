from advent_2021.helpers import get_input


if __name__ == "__main__":
    lines = list(get_input())
    acc = [""] * len(lines[0])
    for line in lines:
        for i, c in enumerate(line):
            acc[i] += c
    print(
        int("".join("1" if c.count("1") > c.count("0") else "0" for c in acc), 2)
        * int("".join("0" if c.count("1") > c.count("0") else "1" for c in acc), 2)
    )
