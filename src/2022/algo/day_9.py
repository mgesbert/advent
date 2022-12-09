def move_head(head, direction):
    return (
        head
        + {
            "U": -1j,
            "R": 1,
            "D": 1j,
            "L": -1,
        }[direction]
    )


def move_tail(head, tail):
    if abs(head - tail) < 2:
        return tail
    if head.real > tail.real:
        tail += 1
    if head.real < tail.real:
        tail -= 1
    if head.imag > tail.imag:
        tail += 1j
    if head.imag < tail.imag:
        tail -= 1j
    return tail


def part_1(input_data):
    visited_pos = {0j}
    head = tail = 0j
    for instruction in input_data:
        direction, steps = instruction.split()
        for _ in range(int(steps)):
            head = move_head(head, direction)
            tail = move_tail(head, tail)
            visited_pos.add(tail)

    return len(visited_pos)


def part_2(input_data):
    visited_pos = {0j}
    rope = [0j] * 10
    for instruction in input_data:
        direction, steps = instruction.split()
        for _ in range(int(steps)):
            rope[0] = move_head(rope[0], direction)
            for i in range(len(rope) - 1):
                rope[i + 1] = move_tail(rope[i], rope[i + 1])
            visited_pos.add(rope[-1])

    return len(visited_pos)
