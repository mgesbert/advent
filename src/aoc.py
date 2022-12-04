import importlib
import os
import sys
from datetime import date
from os.path import dirname, exists, getsize, join

from aocd import get_data


def has_sample():
    sample_path = join(solution_path, 'sample.txt')
    return exists(sample_path) and getsize(sample_path) > 0

def get_sample():
    return get_data_from_file("sample.txt") if has_sample() else None

def get_full_data():
    return get_data_from_file("data.txt")

def get_data_from_file(filename):
    data_path = join(solution_path, filename)
    if not exists(data_path) or getsize(data_path) == 0:
        with open(data_path, 'w') as f:
            f.write(get_data(day=day, year=year) + '\n')

    with open(data_path, 'r') as f:
        for l in f:
            yield l.strip()

def init_solution():
    if not exists(solution_path):
        os.mkdir(solution_path)
        with open(join(solution_path, 'solution.py'), 'w') as f:
            f.write(
                'def part_1(input_data):\n'
                '    list(input_data)\n\n'
                'def part_2(input_data):\n'
                '    list(input_data)'
            )
        with open(join(solution_path, 'sample.txt'), 'w') as f:
            f.write('')



if __name__ == "__main__":
    today = date(int(sys.argv[1]), 12, int(sys.argv[2])) if len(sys.argv) > 1 else date.today()
    day = today.day
    year = today.year

    solution_path = join(dirname(__file__), f"advent_{year}", f"day_{day}")

    init_solution()

    solution = importlib.import_module(f"advent_{year}.day_{day}.solution")

    print('===== Part 1 =====')
    if has_sample():
        print(f" - sample: {solution.part_1(get_sample())}")
    print(f" - data: {solution.part_1(get_full_data())}")
    print()
    print('===== Part 2 =====')
    if has_sample():
        print(f" - sample: {solution.part_2(get_sample())}")
    print(f" - data: {solution.part_2(get_full_data())}")
