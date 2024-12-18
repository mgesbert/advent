out = []


def parse_input(input_data):
    global A, B, C, pointer, program, out
    A = int(next(input_data).split(": ")[1])
    B = int(next(input_data).split(": ")[1])
    C = int(next(input_data).split(": ")[1])
    next(input_data)
    program = [int(i) for i in next(input_data).split(": ")[1].split(",")]
    pointer = 0
    out = []


def combo(op):
    global A, B, C
    if 0 <= op <= 3:
        return op
    if op == 4:
        return A
    if op == 5:
        return B
    if op == 6:
        return C
    if op == 7:
        raise Exception("Invalid combo operand")


def apply_instruction():
    global A, B, C, pointer, program, out
    instr, op = program[pointer : pointer + 2]
    match instr:
        case 0:
            A = A // 2 ** combo(op)
        case 1:
            B ^= op
        case 2:
            B = combo(op) % 8
        case 3:
            if A != 0:
                pointer = op
                return
        case 4:
            B ^= C
        case 5:
            out.append(combo(op) % 8)
        case 6:
            B = A // 2 ** combo(op)
        case 7:
            C = A // 2 ** combo(op)
    pointer += 2


def run_program():
    while pointer < len(program):
        apply_instruction()


def part_1(input_data):
    parse_input(input_data)
    run_program()
    return ",".join(str(i) for i in out)


def dfs(value):
    global A, B, C, pointer, program, out
    A = value
    B = C = pointer = 0
    out = []
    run_program()
    if out == program:
        return value
    if out != program[-len(out) :]:
        return None
    for i in range(8):
        a = dfs((value << 3) + i)
        if a is not None:
            return a
    return None


def part_2(input_data):
    parse_input(input_data)
    for i in range(1, 8):
        a = dfs(i)
        if a is not None:
            return a
