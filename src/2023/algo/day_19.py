import re
import math


def funcify(line):
    name, raw_code = re.search(r"(\w+){(.*)}", line).groups()
    lines_of_code = [
        f"if {s.replace(':', ':return ')}(x,m,a,s)"
        if ":" in s
        else f"return {s}(x,m,a,s)"
        for s in raw_code.split(",")
    ]
    new_line = "\n"
    raw_source_code = (
        f"def {name}(x,m,a,s):{new_line}  {f'{new_line}  '.join(lines_of_code)}"
    )
    return raw_source_code.replace("def in(", "def in_(")


def generate_source_code(input_data, functions):
    source_code = (
        """
def A(x,m,a,s):
    return x + m + a + s

def R(x,m,a,s):
    return 0

"""
        + "\n\n".join(functions)
        + "\n\nprint("
        + " + ".join(f"in_({line[1:-1]})" for line in input_data)
        + ")"
    )
    return source_code


def part_1(input_data):
    functions = []
    for line in input_data:
        if not line:
            break
        functions.append(funcify(line))

    # exec() doesn't work for some reason, but executing the source code works
    print(generate_source_code(input_data, functions))


def combinations(xmas):
    return math.prod(x[1] - x[0] for x in xmas.values())


def update_xmas(xmas, rating, condition, value):
    interval = xmas[rating]
    new_interval = (
        max(interval[0], value + 1) if condition == ">" else interval[0],
        min(interval[1], value) if condition == "<" else interval[1],
    )
    return {**xmas, rating: new_interval}


def complementary(xmas, chunks):
    for rating, condition, value_str, _ in chunks:
        value = int(value_str)
        interval = xmas[rating]
        xmas = {
            **xmas,
            rating: (
                max(interval[0], value) if condition == "<" else interval[0],
                min(interval[1], value + 1) if condition == ">" else interval[1],
            ),
        }
    return xmas


def part_2(input_data):
    lines = []
    for line in input_data:
        if not line:
            break
        lines.append(line)

    intervals = [
        ({"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)}, "in")
        #         x               m               a               s
    ]

    nb_combinations = 0
    while intervals:
        xmas, next_ = intervals.pop(
            next(i for i, (_, v) in enumerate(intervals) if isinstance(v, str))
        )
        try:
            line = next(l for l in lines if l.startswith(next_ + "{"))
        except:
            breakpoint()
        chunks = re.findall(r"([xmas])(<|>)(\d+):(\w+),", line)
        for chunk in chunks:
            rating, condition, value_str, next_op = chunk
            new_xmas = update_xmas(xmas, rating, condition, int(value_str))
            xmas = complementary(xmas, [chunk])
            if next_op == "R":
                continue
            if next_op == "A":
                nb_combinations += combinations(new_xmas)
                continue
            intervals.append((new_xmas, next_op))

        new_xmas = complementary(xmas, chunks)
        next_op = line.split(",")[-1][:-1]
        if next_op == "A":
            nb_combinations += combinations(new_xmas)
        elif next_op != "R":
            intervals.append((new_xmas, next_op))

    return nb_combinations
