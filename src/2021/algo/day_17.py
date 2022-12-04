def part_1(input_data):
    def max_height_reached(dy: int, y0: int, y1: int) -> int:
        y = 0
        max_y = 0
        while (y := y + dy) > y1:
            max_y = max(y, max_y)
            dy -= 1
        return max_y if y >= y0 else 0

    x0, x1, y0, y1 = [
        int(boundary)
        for range_ in next(input_data)
        .split(": ")[1]
        .replace("x=", "")
        .replace("y=", "")
        .split(", ")
        for boundary in range_.split("..")
    ]
    return max([max_height_reached(dy, y0, y1) for dy in range(1000)])


def part_2(input_data):
    def target_reached(dx: int, dy: int, x0: int, x1: int, y0: int, y1: int) -> bool:
        x, y = 0, 0
        while x < x0 and dx > 0 or y > y1:
            x += dx
            y += dy
            dx = dx - 1 if dx > 0 else dx + 1 if dx < 0 else 0
            dy -= 1
        return x0 <= x <= x1 and y0 <= y <= y1

    x0, x1, y0, y1 = [
        int(boundary)
        for range_ in next(input_data)
        .split(": ")[1]
        .replace("x=", "")
        .replace("y=", "")
        .split(", ")
        for boundary in range_.split("..")
    ]
    return sum(
        target_reached(dx, dy, x0, x1, y0, y1)
        for dx in range(1, 300)
        for dy in range(-300, 300)
    )
