from advent_2021.helpers import get_input


def target_reached(dx: int, dy: int, x0: int, x1: int, y0: int, y1: int) -> bool:
    x, y = 0, 0
    while x < x0 and dx > 0 or y > y1:
        x += dx
        y += dy
        dx = dx - 1 if dx > 0 else dx + 1 if dx < 0 else 0
        dy -= 1
    return x0 <= x <= x1 and y0 <= y <= y1


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
    print(
        sum(
            target_reached(dx, dy, x0, x1, y0, y1)
            for dx in range(1, 300)
            for dy in range(-300, 300)
        )
    )
