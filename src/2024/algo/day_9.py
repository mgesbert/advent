def block_id(position):
    return position // 2


def sector_checksum(start, length, id):
    return ((start + length - 1) * (start + length) - (start - 1) * start) // 2 * id


def part_1(input_data):
    disk_map = [int(x) for x in next(input_data)]
    disk_size = sum(disk_map[::2])

    position = 0
    left_cursor = 0
    right_cursor = len(disk_map) - 1

    check_sum = 0

    while position < disk_size:
        if left_cursor % 2 == 0:  # file block
            check_sum += sector_checksum(
                position, disk_map[left_cursor], block_id(left_cursor)
            )
            position += disk_map[left_cursor]
            left_cursor += 1
        else:  # directory block
            n = min(disk_map[right_cursor], disk_map[left_cursor])
            disk_map[right_cursor] -= n
            disk_map[left_cursor] -= n

            check_sum += sector_checksum(position, n, block_id(right_cursor))
            position += n

            if disk_map[right_cursor] == 0:
                right_cursor -= 2
            if disk_map[left_cursor] == 0:
                left_cursor += 1
    return check_sum


def part_2(input_data):
    disk_map = [int(x) for x in next(input_data)]
    original_disk_map = [*disk_map]

    position = 0
    left_cursor = 0
    right_cursor = len(disk_map) - 1
    used_space = 0

    check_sum = 0

    while left_cursor < len(disk_map):
        if left_cursor % 2 == 0:  # file block
            if disk_map[left_cursor] > 0:
                check_sum += sector_checksum(
                    position, disk_map[left_cursor], block_id(left_cursor)
                )
            position += original_disk_map[left_cursor]
            left_cursor += 1
        else:  # directory block
            right_cursor = next(
                (
                    i
                    for i in range(len(disk_map) - 1, left_cursor, -2)
                    if 0 < disk_map[i] <= disk_map[left_cursor] - used_space
                ),
                None,
            )

            if right_cursor is None:
                position += original_disk_map[left_cursor] - used_space
                left_cursor += 1
                used_space = 0
            else:
                check_sum += sector_checksum(
                    position, disk_map[right_cursor], block_id(right_cursor)
                )
                used_space += disk_map[right_cursor]
                position += disk_map[right_cursor]
                disk_map[right_cursor] = 0
    return check_sum
