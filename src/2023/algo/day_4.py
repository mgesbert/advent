def score(line):
    numbers = [x.split() for x in line.split("|")]
    return sum(a in numbers[0] for a in numbers[1])


def part_1(input_data):
    return sum(2 ** (s - 1) for s in map(score, input_data) if s > 0)


def part_2(input_data):
    lines = list(input_data)
    acc = [1] * len(lines)
    for i, line in enumerate(lines):
        for j in range(i + 1, i + score(line) + 1):
            acc[j] += acc[i]
    return sum(acc)
