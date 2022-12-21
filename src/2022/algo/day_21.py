import re

from sympy import Symbol
from sympy.solvers import solve


def part_1(input_data):
    data = dict(line.split(": ") for line in input_data)
    expr = data["root"]
    while re.search("[a-zA-Z]", expr):
        for k, v in data.items():
            if k in expr:
                expr = expr.replace(k, f"({v})")
    return int(eval(expr))


def part_2(input_data):
    data = dict(line.split(": ") for line in input_data)
    data["root"] = data["root"].replace("+", "-").replace("/", "-").replace("*", "-")
    data["humn"] = "humn"
    expr = data["root"]
    while re.search("[a-zA-Z]", expr.replace("humn", "")):
        for k, v in data.items():
            if k in expr:
                expr = expr.replace(k, f"({v})")
    humn = Symbol(name="humn")
    return int(solve(eval(expr))[0])


# Alternative solution for part 1

# def yell(monkeys, monkey):
#     if isinstance(monkey, int):
#         return monkey
#     m1, op, m2 = monkey
#     return eval(f"int({yell(monkeys, monkeys[m1])} {op} {yell(monkeys, monkeys[m2])})")


# def part_1(input_data):
#     monkeys = {
#         name: int(value) if value.isdigit() else value.split()
#         for name, value in [line.split(": ") for line in input_data]
#     }
#     return yell(monkeys, monkeys["root"])
