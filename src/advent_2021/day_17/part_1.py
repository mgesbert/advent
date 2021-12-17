from advent_2021.helpers import get_input


def max_height_reached(dy: int, y0: int, y1: int) -> int:
    y = 0
    max_y = 0
    while (y := y + dy) > y1:
        max_y = max(y, max_y)
        dy -= 1
    return max_y if y >= y0 else 0


if __name__ == "__main__":
    x0, x1, y0, y1 = [
        int(boundary)
        for range_ in next(get_input())
        .split(": ")[1]
        .replace("x=", "")
        .replace("y=", "")
        .split(", ")
        for boundary in range_.split("..")
    ]
    print(max([max_height_reached(dy, y0, y1) for dy in range(1000)]))
