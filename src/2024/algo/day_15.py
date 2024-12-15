DIRECTIONS = {
    ">": 1,
    "<": -1,
    "^": -1j,
    "v": 1j,
}


def parse_input(input_data):
    boxes, walls = set(), set()
    instructions = ""
    for j, line in enumerate(input_data):
        if not line.startswith("#"):
            instructions += line.strip()
            continue

        for i, c in enumerate(line):
            if c == ".":
                continue
            pos = i + 1j * j
            if c == "O":
                boxes.add(pos)
            elif c == "#":
                walls.add(pos)
            elif c == "@":
                start = pos
    return boxes, walls, start, instructions


def move_boxes(boxes, walls, z, instructions):
    for instruction in instructions:
        dz = DIRECTIONS[instruction]
        if z + dz in boxes:
            box = z + dz
            while box in boxes:
                box += dz
            if box not in walls:
                boxes.remove(z + dz)
                boxes.add(box)
                z += dz
        elif z + dz not in walls:
            z += dz
    return boxes


def part_1(input_data):
    boxes, walls, start, instructions = parse_input(input_data)
    end_boxes = move_boxes(boxes, walls, start, instructions)
    return sum((100 * int(round(box.imag)) + int(round(box.real))) for box in end_boxes)


def parse_input_2(input_data):
    boxes = set()
    walls = set()
    instructions = ""
    for j, line in enumerate(input_data):
        if line.startswith("#"):
            for i, c in enumerate(line):
                if c != ".":
                    if c == "O":
                        boxes.add((2 * i + 1j * j, 2 * i + 1 + 1j * j))
                    elif c == "#":
                        walls.add(2 * i + 1j * j)
                        walls.add(2 * i + 1 + 1j * j)
                    elif c == "@":
                        start = 2 * i + 1j * j
        elif line.strip():
            instructions += line
    return boxes, walls, start, instructions


def debug_print(boxes, walls, z):
    width = int(round(max(wall.real for wall in walls))) + 1
    height = int(round(max(wall.imag for wall in walls))) + 1
    s = ""
    for j in range(height):
        for i in range(width):
            if i + 1j * j == z:
                s += "@"
            elif any(b1 == i + 1j * j for b1, _ in boxes):
                s += "["
            elif any(b2 == i + 1j * j for _, b2 in boxes):
                s += "]"
            elif i + 1j * j in walls:
                s += "#"
            else:
                s += " "
        s += "\n"
    print(s)


def part_2(input_data):
    boxes, walls, start, instructions = parse_input_2(input_data)
    end_boxes = move_boxes_2(
        boxes,
        walls,
        start,
        instructions,
    )
    return sum((100 * int(round(b1.imag)) + int(round(b1.real))) for b1, _ in end_boxes)


def move_boxes_2(
    boxes,
    walls,
    z,
    instructions,
):
    for instruction in instructions:
        dz = DIRECTIONS[instruction]
        if z + dz in walls:
            continue
        stack = [(b1 + dz, b2 + dz) for b1, b2 in boxes if b1 == z + dz or b2 == z + dz]
        boxes_to_remove = {(b1, b2) for b1, b2 in boxes if b1 == z + dz or b2 == z + dz}
        boxes_to_add = set()
        while stack:
            next_b = stack.pop()
            boxes_to_add.add(next_b)
            b1, b2 = next_b
            if b1 in walls or b2 in walls:
                break
            pushed_boxes = {
                (bb1, bb2)
                for bb1, bb2 in boxes
                if (bb1 == b1 or bb2 == b1 or bb1 == b2 or bb2 == b2)
                and (bb1, bb2) not in boxes_to_remove
            }
            for bb1, bb2 in pushed_boxes:
                stack.append((bb1 + dz, bb2 + dz))
                boxes_to_remove.add((bb1, bb2))
        else:
            boxes = boxes - boxes_to_remove | boxes_to_add
            z += dz

        # debug_print(boxes, walls, z)
    return boxes
