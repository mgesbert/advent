from functools import lru_cache


# TODO execution time is long, improve it

Position = tuple[int, int, int]


def manhattan_dist(a: tuple[int, int, int], b: tuple[int, int, int]):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def rotate_result(scan_result: tuple[Position, ...]):
    return [
        tuple(sorted((x, y, z) for x, y, z in scan_result)),
        tuple(sorted((x, z, -y) for x, y, z in scan_result)),
        tuple(sorted((x, -y, -z) for x, y, z in scan_result)),
        tuple(sorted((x, -z, y) for x, y, z in scan_result)),
        tuple(sorted((-x, y, -z) for x, y, z in scan_result)),
        tuple(sorted((-x, -z, -y) for x, y, z in scan_result)),
        tuple(sorted((-x, -y, z) for x, y, z in scan_result)),
        tuple(sorted((-x, z, y) for x, y, z in scan_result)),
        tuple(sorted((y, -x, z) for x, y, z in scan_result)),
        tuple(sorted((y, z, x) for x, y, z in scan_result)),
        tuple(sorted((y, x, -z) for x, y, z in scan_result)),
        tuple(sorted((y, -z, -x) for x, y, z in scan_result)),
        tuple(sorted((-y, -x, -z) for x, y, z in scan_result)),
        tuple(sorted((-y, -z, x) for x, y, z in scan_result)),
        tuple(sorted((-y, x, z) for x, y, z in scan_result)),
        tuple(sorted((-y, z, -x) for x, y, z in scan_result)),
        tuple(sorted((z, y, -x) for x, y, z in scan_result)),
        tuple(sorted((z, -x, -y) for x, y, z in scan_result)),
        tuple(sorted((z, -y, x) for x, y, z in scan_result)),
        tuple(sorted((z, x, y) for x, y, z in scan_result)),
        tuple(sorted((-z, y, x) for x, y, z in scan_result)),
        tuple(sorted((-z, x, -y) for x, y, z in scan_result)),
        tuple(sorted((-z, -y, -x) for x, y, z in scan_result)),
        tuple(sorted((-z, -x, y) for x, y, z in scan_result)),
    ]


@lru_cache(maxsize=1000000)  # useless?
def overlap_size(
    scan_result_1: tuple[Position, ...], scan_result_2: tuple[Position, ...]
) -> int:
    scan_result_1 = tuple(sorted(scan_result_1))
    scan_result_2 = tuple(sorted(scan_result_2))
    i = j = 0
    count = 0
    while i < len(scan_result_1) and j < len(scan_result_2):
        count += scan_result_1[i] == scan_result_2[j]
        if scan_result_1[i] <= scan_result_2[j]:
            i += 1
        else:
            j += 1
    return count


def part_1(input_data):
    def candidate_scanner_positions(
        scan_result: tuple[Position, ...], know_beacons: tuple[Position, ...]
    ) -> set[Position]:
        return {
            (X - x, Y - y, Z - z)
            for (x, y, z) in scan_result
            for (X, Y, Z) in know_beacons
        }

    scan_results: list[list[Position]] = []
    scan_result: list[Position] = []
    for line in input_data:
        if line == "":
            scan_results.append(sorted(scan_result))
            scan_result = []
            continue
        if line.startswith("--"):
            continue
        position = tuple(map(int, line.split(",")))
        if len(position) != 3:
            raise ValueError
        scan_result.append(position)  # type: ignore
    scan_results.append(sorted(scan_result))

    scanner_positions: dict[int, Position] = {0: (0, 0, 0)}
    known_beacons = tuple(scan_results[0])

    for _ in range(len(scan_results) - 1):
        for i, scan_result in enumerate(scan_results):
            beacons = tuple(scan_result)
            if i in scanner_positions:
                continue

            for rotated_positions in rotate_result(beacons):
                x0, y0, z0 = max(
                    candidate_scanner_positions(rotated_positions, known_beacons),
                    key=lambda pos: overlap_size(
                        tuple(
                            [
                                (x + pos[0], y + pos[1], z + pos[2])
                                for x, y, z in rotated_positions
                            ]
                        ),
                        known_beacons,
                    ),
                )
                absolute_beacon_positions = tuple(
                    [(x + x0, y + y0, z + z0) for x, y, z in rotated_positions]
                )
                if (
                    overlap_size(
                        absolute_beacon_positions,
                        known_beacons,
                    )
                    < 12
                ):
                    continue
                known_beacons = tuple(
                    set(known_beacons) | set(absolute_beacon_positions)
                )
                scanner_positions[i] = (x0, y0, z0)

    return len(known_beacons)


def part_2(input_data):
    def candidate_scanner_positions(
        scan_result: tuple[Position, ...], know_beacons: tuple[Position, ...]
    ) -> set[Position]:
        return {
            (X - x, Y - y, Z - z)
            for (x, y, z) in scan_result
            for (X, Y, Z) in know_beacons
        }

    scan_results: list[list[Position]] = []
    scan_result: list[Position] = []
    for line in input_data:
        if line == "":
            scan_results.append(sorted(scan_result))
            scan_result = []
            continue
        if line.startswith("--"):
            continue
        position = tuple(map(int, line.split(",")))
        if len(position) != 3:
            raise ValueError
        scan_result.append(position)  # type: ignore
    scan_results.append(sorted(scan_result))

    scanner_positions: dict[int, Position] = {0: (0, 0, 0)}
    known_beacons = tuple(scan_results[0])

    for _ in range(len(scan_results) - 1):
        for i, scan_result in enumerate(scan_results):
            beacons = tuple(scan_result)
            if i in scanner_positions:
                continue

            for rotated_positions in rotate_result(beacons):
                x0, y0, z0 = max(
                    candidate_scanner_positions(rotated_positions, known_beacons),
                    key=lambda pos: overlap_size(
                        tuple(
                            [
                                (x + pos[0], y + pos[1], z + pos[2])
                                for x, y, z in rotated_positions
                            ]
                        ),
                        known_beacons,
                    ),
                )
                absolute_beacon_positions = tuple(
                    [(x + x0, y + y0, z + z0) for x, y, z in rotated_positions]
                )
                if (
                    overlap_size(
                        absolute_beacon_positions,
                        known_beacons,
                    )
                    < 12
                ):
                    continue
                known_beacons = tuple(
                    set(known_beacons) | set(absolute_beacon_positions)
                )
                scanner_positions[i] = (x0, y0, z0)

    return max(
        manhattan_dist(pos1, pos2)
        for pos1 in scanner_positions.values()
        for pos2 in scanner_positions.values()
    )
