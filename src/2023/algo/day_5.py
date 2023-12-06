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
                dest + result - origin
                for dest, origin, count in mapping
                if origin <= result < origin + count
            ),
            result,
        )
    return result


def part_1(input_data):
    seeds, mappings = parse_input(input_data)
    return min(find_location(seed, mappings) for seed in seeds)


def get_next_ranges(seed_start, seed_count, mapping):
    stack = [(seed_start, seed_count)]
    while stack:
        seed_start, seed_count = stack.pop(0)
        for dest, origin, count in mapping:
            if origin <= seed_start < origin + count:
                yield dest + seed_start - origin, min(
                    seed_count, origin + count - seed_start
                )
                if seed_start + seed_count >= origin + count:
                    stack.append(
                        (origin + count, seed_count - (origin + count - seed_start))
                    )
                break
        else:
            yield seed_start, seed_count


def part_2(input_data):
    seeds, mappings = parse_input(input_data)
    locations = []
    for seed_start, seed_count in zip(seeds[::2], seeds[1::2]):
        ranges = [(seed_start, seed_count)]
        for mapping in mappings:
            ranges = [
                x
                for s_start, s_count in ranges
                for x in get_next_ranges(s_start, s_count, mapping)
            ]
        locations.extend(location for location, _ in ranges)
    return min(locations)
