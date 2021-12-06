from advent_2020.helpers import get_input


if __name__ == "__main__":
    instructions = [(o[0], int(o[1:])) for o in get_input()]
    wp_x = 10
    wp_y = -1
    x = y = 0
    for order, value in instructions:
        if order == "E":
            wp_x += value
        if order == "N":
            wp_y -= value
        if order == "W":
            wp_x -= value
        if order == "S":
            wp_y += value
        if order == "L":
            for _ in range(value // 90):
                tmp = wp_x
                wp_x = wp_y
                wp_y = -tmp
        if order == "R":
            for _ in range(value // 90):
                tmp = wp_x
                wp_x = -wp_y
                wp_y = tmp
        if order == "F":
            x += wp_x * value
            y += wp_y * value
    print(abs(x) + abs(y))
