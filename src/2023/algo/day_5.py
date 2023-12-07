def parse_input(input_data):
    seeds = [int(x) for x in next(input_data).split()[1:]]

    result = []
    for line in input_data:
        if not line.strip():
            result.append([])
            next(input_data)
            continue
        result[-1].append(tuple(int(x) for x in line.split()))

    return seeds, [sorted(m, key=lambda x: x[1]) for m in result]


def find_location(seed, mappings):
    result = seed
    for mapping in mappings:
        result = next(
            (
                dest + result - start
                for dest, start, count in mapping
                if start <= result < start + count
            ),
            result,
        )
    return result


def next_ranges(seed_start, seed_count, mapping):
    stack = [(seed_start, seed_count)]
    while stack:
        seed_start, seed_count = stack.pop(0)
        for dest, start, count in mapping:
            if start <= seed_start < start + count:
                yield dest + seed_start - start, min(
                    seed_count, start + count - seed_start
                )
                if seed_start + seed_count >= start + count:
                    stack.append(
                        (start + count, seed_count - (start + count - seed_start))
                    )
                break
        else:
            yield seed_start, seed_count


def find_locations(seed_start, seed_count, mappings):
    ranges = [(seed_start, seed_count)]
    for mapping in mappings:
        ranges = [
            x
            for s_start, s_count in ranges
            for x in next_ranges(s_start, s_count, mapping)
        ]
    return [location for location, _ in ranges]


def part_1(input_data):
    seeds, mappings = parse_input(input_data)
    return min(
        find_locations(seed_start, seed_count, mappings)[0]
        for seed_start, seed_count in zip(seeds[::2], seeds[1::2])
    )


def part_2(input_data):
    seeds, mappings = parse_input(input_data)
    return min(
        location
        for seed_start, seed_count in zip(seeds[::2], seeds[1::2])
        for location in find_locations(seed_start, seed_count, mappings)
    )
