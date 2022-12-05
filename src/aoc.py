import importlib
import sys
from datetime import date
from os.path import dirname, exists, getsize, join

from aocd import get_data as get_data_from_aoc


def parse_args():
    today = (
        date(int(sys.argv[1]), 12, int(sys.argv[2]))
        if len(sys.argv) > 1
        else date.today()
    )
    return today.day, today.year


def has_sample():
    return any(get_sample())


def get_sample():
    with open(sample_file, "r") as f:
        for l in f:
            yield l


def get_data():
    if not exists(data_file) or getsize(data_file) == 0:
        with open(data_file, "w") as f:
            f.write(get_data_from_aoc(day=day, year=year) + "\n")

    with open(data_file, "r") as f:
        for l in f:
            yield l


def init_solution():
    if not exists(solution_file):
        with open(solution_file, "w") as f:
            f.write(
                "def part_1(input_data):\n"
                "    list(input_data)\n\n"
                "def part_2(input_data):\n"
                "    list(input_data)"
            )

    # init this file as there is no way to fetch it automatically
    # there is no other way than copy/pasting the sample data in it
    if not exists(sample_file):
        with open(sample_file, "w") as f:
            f.write("")


if __name__ == "__main__":
    day, year = parse_args()

    solution_file = join(dirname(__file__), str(year), "algo", f"day_{day}.py")
    data_file = join(dirname(__file__), str(year), "data", f"day_{day}.txt")
    sample_file = join(dirname(__file__), str(year), "sample", f"day_{day}.txt")

    init_solution()

    solution = importlib.import_module(f"{year}.algo.day_{day}")

    print("===== Part 1 =====")
    if has_sample():
        print(f" - sample: {solution.part_1(get_sample())}")
    print(f" - data: {solution.part_1(get_data())}")
    print()
    print("===== Part 2 =====")
    if has_sample():
        print(f" - sample: {solution.part_2(get_sample())}")
    print(f" - data: {solution.part_2(get_data())}")
