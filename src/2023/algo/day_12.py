from functools import cache


def parse_line(line, factor):
    data, counts = line.split(" ")
    counts = tuple(int(x) for x in counts.split(","))
    return "?".join([data] * factor), counts * factor


@cache
def nb_arrangements(data, counts, acc=0):
    if len(data) == 0:
        return len(counts) == 0 and acc == 0 or len(counts) == 1 and acc == counts[0]
    if counts and acc > counts[0]:
        return 0
    total = 0
    for c in "#." if data[0] == "?" else data[0]:
        if c == "#" and counts:
            total += nb_arrangements(data[1:], counts, acc + 1)
        if c == ".":
            if acc > 0:
                if len(counts) > 0 and acc == counts[0]:
                    total += nb_arrangements(data[1:], counts[1:], 0)
            else:
                total += nb_arrangements(data[1:], counts, 0)
    return total


def part_1(input_data):
    return sum(nb_arrangements(*parse_line(line, 1)) for line in input_data)


def part_2(input_data):
    return sum(nb_arrangements(*parse_line(line, 5)) for line in input_data)
