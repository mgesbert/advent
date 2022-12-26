from collections import defaultdict


NORTH = -1j
SOUTH = 1j
WEST = -1
EAST = 1
NEIGHBORS = {
    NORTH: [NORTH + WEST, NORTH, NORTH + EAST],
    SOUTH: [SOUTH + WEST, SOUTH, SOUTH + EAST],
    WEST: [NORTH + WEST, WEST, SOUTH + WEST],
    EAST: [NORTH + EAST, EAST, SOUTH + EAST],
}
ALL_NEIGHBORS = set(d for l in NEIGHBORS.values() for d in l)


def debug(elves):
    min_x = int(min(e.real for e in elves))
    max_x = int(max(e.real for e in elves))
    min_y = int(min(e.imag for e in elves))
    max_y = int(max(e.imag for e in elves))
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print("#" if (x + y * 1j) in elves else ".", end="")
        print()
    print()


def solve(input_data, max_turns):
    directions = [NORTH, SOUTH, WEST, EAST]
    elves = {
        x + y * 1j
        for y, line in enumerate(input_data)
        for x, c in enumerate(line)
        if c == "#"
    }
    turn = 1
    previous_elves = set()
    while elves != previous_elves and turn <= max_turns:
        previous_elves = elves
        next_positions = {e: e for e in elves}
        next_position_counts = defaultdict(int)
        for elf in elves:
            if all(elf + n not in elves for n in ALL_NEIGHBORS):
                continue
            for direction in directions:
                if any(elf + n in elves for n in NEIGHBORS[direction]):
                    continue
                next_positions[elf] = elf + direction
                next_position_counts[elf + direction] += 1
                break

        elves = {
            v if next_position_counts[v] == 1 else k for k, v in next_positions.items()
        }
        directions = directions[1:] + directions[:1]
        turn += 1

    return elves, turn


def part_1(input_data):
    elves, _ = solve(input_data, 10)

    return int(
        round(max(e.real for e in elves) - min(e.real for e in elves) + 1)
        * round(max(e.imag for e in elves) - min(e.imag for e in elves) + 1)
    ) - len(elves)


def part_2(input_data):
    _, turn = solve(input_data, float("inf"))

    return turn - 1
