from advent_2021.helpers import get_input


if __name__ == "__main__":
    lines = list(get_input())
    print(
        sum(
            int(c) + 1
            for y, line in enumerate(lines)
            for x, c in enumerate(line)
            if (x == 0 or c < line[x - 1])
            and (x == len(line) - 1 or c < line[x + 1])
            and (y == 0 or c < lines[y - 1][x])
            and (y == len(lines) - 1 or c < lines[y + 1][x])
        )
    )
