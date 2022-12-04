from advent_2020.helpers import get_input


DIRECTIONS = "ENWS"

if __name__ == "__main__":
    instructions = [(o[0], int(o[1:])) for o in get_input()]
    x = y = 0
    dir_index = 0
    for order, value in instructions:
        if order == "E":
            x += value
        if order == "N":
            y -= value
        if order == "W":
            x -= value
        if order == "S":
            y += value
        if order == "L":
            dir_index = (dir_index + value // 90) % 4
        if order == "R":
            dir_index = (dir_index - value // 90) % 4
        if order == "F":
            direction = DIRECTIONS[dir_index]
            x += ((direction == "E") - (direction == "W")) * value
            y += ((direction == "S") - (direction == "N")) * value
    print(abs(x) + abs(y))
