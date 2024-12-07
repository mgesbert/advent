import itertools
from functools import reduce


def parse_input(input_data):
    result = []
    for line in input_data:
        left, right = line.split(": ")
        result.append((int(left), list(map(int, right.split(" ")))))
    return result


def apply_operator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "*":
        return a * b
    elif operator == "|":
        return int(f"{a}{b}")


def are_operators_valid(left, right, operators):
    if len(operators) != len(right) - 1:
        raise ValueError(f"Invalid operators: {operators} {right}")

    def accumulate(acc, value_op):
        if acc > left:
            return acc
        value, operator = value_op
        return apply_operator(acc, value, operator)

    return left == reduce(accumulate, zip(right[1:], operators), right[0])


def solve_for(input_data, operators):
    equations = parse_input(input_data)
    return sum(
        left
        for left, right in equations
        if any(
            are_operators_valid(left, right, operators)
            for operators in itertools.product(operators, repeat=len(right) - 1)
        )
    )


def part_1(input_data):
    return solve_for(input_data, "+*")


def part_2(input_data):
    return solve_for(input_data, "+*|")
