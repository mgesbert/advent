def parse_input(input_data):
    input_data = list(input_data)
    height = len(input_data)
    width = len(input_data[0])
    blocks = {
        x + y * 1j: int(c)
        for y, row in enumerate(input_data)
        for x, c in enumerate(row)
    }
    return blocks, height, width


def dijkstra(blocks, height, width, min_steps, max_steps):
    queue = [(0, 0, None, 10)]
    visited = set()
    while queue:
        (heat_loss, z, direction, straight_steps), *queue = queue
        if (z, direction, straight_steps) in visited:
            continue
        visited |= {(z, direction, straight_steps)}

        if z == width - 1 + (height - 1) * 1j:
            return heat_loss

        candidates = (
            {min_steps, min_steps * 1j}
            if direction is None
            else {
                z + direction,
                z + 1j * min_steps * direction,
                z - 1j * min_steps * direction,
            }
            if straight_steps < max_steps
            else {
                z + 1j * min_steps * direction,
                z - 1j * min_steps * direction,
            }
        )

        for next_z in candidates:
            if (next_z, next_z - z) in visited:
                continue
            if not (0 <= next_z.real < width and 0 <= next_z.imag < height):
                continue

            next_ss = (
                (straight_steps + 1)
                if direction is not None and z + direction == next_z
                else min_steps
            )

            try:
                queue.append(
                    (
                        heat_loss + heat_loss_over(blocks, z, next_z),
                        next_z,
                        (next_z - z) / abs(next_z - z),
                        next_ss,
                    ),
                )
            except:
                print(z, next_z, width, height)

        queue.sort(key=lambda x: x[0])


def heat_loss_over(blocks, start, end):
    x = start
    delta = (end - start) / abs(end - start)
    result = 0
    while start != end:
        start += delta
        result += blocks[start]
    return result


def part_1(input_data):
    return dijkstra(*parse_input(input_data), 1, 3)


def part_2(input_data):
    return dijkstra(*parse_input(input_data), 4, 10)
