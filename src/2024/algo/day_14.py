import math
import re
import time


def parse_input(input_data):
    return [
        [
            int(x)
            for x in re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups()
        ]
        for line in input_data
    ]


def move_robots(robots, width, height, time):
    return [
        ((x + vx * time) % width, (y + vy * time) % height) for x, y, vx, vy in robots
    ]


def compute_safety_factor(robots, width, height):
    top_left = top_right = bottom_left = bottom_right = 0
    for robot in robots:
        x, y = robot
        if x < (width - 1) / 2 and y < (height - 1) / 2:
            top_left += 1
        elif x < (width - 1) / 2 and y > (height - 1) / 2:
            bottom_left += 1
        elif x > (width - 1) / 2 and y < (height - 1) / 2:
            top_right += 1
        elif x > (width - 1) / 2 and y > (height - 1) / 2:
            bottom_right += 1
    return top_left * top_right * bottom_left * bottom_right


def part_1(input_data):
    robots = parse_input(input_data)
    width = 11 if max(x for x, _, _, _ in robots) < 15 else 101
    height = 7 if max(y for _, y, _, _ in robots) < 15 else 103
    robots_at_100 = move_robots(robots, width, height, 100)
    return compute_safety_factor(robots_at_100, width, height)


def display_robots(robots, width, height, i):
    image = "┌" + "─" * width + "┐\n"
    image += (
        f"│ seconds ellapsed: {i}" + " " * (width - 21 - int(math.log10(i))) + " │\n"
    )
    image += "├" + "─" * width + "┤\n"
    for y in range(height):
        image += "│"
        for x in range(width):
            if (x, y) in robots:
                image += "█"
            else:
                image += " "
        image += "│\n"
    image += "└" + "─" * width + "┘\n"
    print(image)


def part_2(input_data):
    robots = parse_input(input_data)
    if max(x for x, _, _, _ in robots) < 15:
        return
    width = 101
    height = 103
    i = 65
    while True:
        # watch the pictures in the terminal, and break when you see the christmas tree
        display_robots(move_robots(robots, width, height, i), width, height, i)
        i += 103
        time.sleep(0.05)
