def parse_stacks(input_data):
    stacks_input = []
    while "[" in (line := next(input_data)):
        stacks_input.append(line)
    nb_stacks = len(line.split())
    stacks = [
        [line[i] for line in stacks_input[::-1] if i < len(line) and line[i] != " "]
        for i in [4 * x + 1 for x in range(nb_stacks)]
    ]
    next(input_data)

    return stacks


def part_1(input_data):
    stacks = parse_stacks(input_data)

    for instruction in input_data:
        tokens = instruction.split()
        nb, stack_from, stack_to = [
            int(tokens[1]),
            int(tokens[3]) - 1,
            int(tokens[5]) - 1,
        ]
        stacks[stack_to] += stacks[stack_from][-nb:][::-1]
        stacks[stack_from] = stacks[stack_from][:-nb]
    return "".join(s[-1] for s in stacks)


def part_2(input_data):
    stacks = parse_stacks(input_data)

    for instruction in input_data:
        tokens = instruction.split()
        nb, stack_from, stack_to = [
            int(tokens[1]),
            int(tokens[3]) - 1,
            int(tokens[5]) - 1,
        ]
        stacks[stack_to] += stacks[stack_from][-nb:]
        stacks[stack_from] = stacks[stack_from][:-nb]
    return "".join(s[-1] for s in stacks)
