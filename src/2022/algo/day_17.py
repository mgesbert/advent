from line_profiler import LineProfiler


profiler = LineProfiler()


def profile(func):
    def inner(*args, **kwargs):
        profiler.add_function(func)
        profiler.enable_by_count()
        return func(*args, **kwargs)

    return inner


def print_stats():
    profiler.print_stats()


BLOCKS = [
    [0, 1, 2, 3],
    [1j, 1, 1 + 1j, 1 + 2j, 2 + 1j],
    [0, 1, 2, 2 + 1j, 2 + 2j],
    [0, 1j, 2j, 3j],
    [0, 1j, 1, 1 + 1j],
]


def debug(occupied):
    max_y = int(max(c.imag for c in occupied))
    for y in range(max_y, -1, -1):
        for x in range(7):
            print("#" if x + 1j * y in occupied else ".", end="")
        print()


def can_slide(offset, block, occupied, x, y):
    if not all(0 <= int(round(b.real)) + x + offset < 7 for b in block):
        return False
    for c in occupied:
        if abs(block[0] + x + y * 1j - c) > 5:
            continue
        for b in block:
            if c == b + x + y * 1j + offset:
                return False
    return True


def can_fall(block, occupied, x, y):
    for c in occupied:
        if abs(block[0] + x + y * 1j - c) > 5:
            continue
        for b in block:
            if c == b + x + y * 1j - 1j:
                return False
    return True


def compute_key_first_block(nb_instructions, step, occupied):
    return (
        step % nb_instructions,
        tuple(sorted(occupied, key=lambda c: (c.imag, c.real), reverse=True)),
    )


def fall(instructions, i, step, occupied):
    max_y = int(max(c.imag for c in occupied))
    y = max_y + 4
    x = 2
    block = BLOCKS[i % 5]
    while True:
        offset = 1 if instructions[step % len(instructions)] == ">" else -1
        step += 1
        if can_slide(offset, block, occupied, x, y):
            x += offset
        if can_fall(block, occupied, x, y):
            y -= 1
        else:
            for b in block:
                occupied.add(b + x + y * 1j)
            return occupied, step


def part_1(input_data):
    instructions = next(input_data)
    occupied = {0, 1, 2, 3, 4, 5, 6}
    step = 0
    for i in range(2022):
        occupied, step = fall(instructions, i, step, occupied)
        max_y = int(max(c.imag for c in occupied))
        to_remove = set()
        for c in occupied:
            if abs(c - max_y * 1j) > 40:
                to_remove.add(c)
        occupied -= to_remove
    return int(max(c.imag for c in occupied))


def part_2(input_data):
    nb_blocks = 1000000000000
    instructions = next(input_data)
    occupied = {0, 1, 2, 3, 4, 5, 6}
    step = 0
    cache = {}
    y_offset = 0
    i = 0
    while i < nb_blocks:
        if i % 100 == 0:
            print(i)
        occupied, step = fall(instructions, i, step, occupied)

        if i % 5 > 0:
            i += 1
            continue

        max_y = int(max(c.imag for c in occupied))
        if max_y > 200:
            occupied = {
                c - (max_y - 200) * 1j for c in occupied if abs(max_y - c.imag) <= 200
            }
            y_offset += max_y - 200

        key = compute_key_first_block(len(instructions), step, occupied)
        if key in cache:
            cycle_len = i - cache[key]["i"]
            full_cycles_remaining = (nb_blocks - i) // cycle_len
            delta_y = max_y + y_offset - cache[key]["max_y"]
            i += cycle_len * full_cycles_remaining
            y_offset += delta_y * full_cycles_remaining

        cache[key] = {"max_y": max_y + y_offset, "i": i}
        i += 1

    return int(max(c.imag for c in occupied)) + y_offset
