import re
from functools import lru_cache
from typing import Any


def part_1(input_data):
    def explode_replace(number: str, to_add: int, reverse: bool):
        if reverse:
            number = number[::-1]
        match = re.search(r"\d+", number)
        if match is None:
            return number[::-1] if reverse else number
        matched = number[match.start() : match.end()]
        replace_value = (
            str(int(matched[::-1]) + to_add)[::-1]
            if reverse
            else str(int(matched) + to_add)
        )
        replaced = (
            number.replace(matched, replace_value, 1)[::-1]
            if reverse
            else number.replace(matched, replace_value, 1)
        )
        return replaced

    def explode(number: str, i: int) -> str:
        match = re.search(r"^\[(\d+),(\d+)\]", number[i:])
        if match is None:
            raise ValueError(number[i:])
        left = explode_replace(number[:i], int(match.groups()[0]), True)
        right = explode_replace(
            number[match.end() + i :], int(match.groups()[1]), False
        )
        return f"{left}0{right}"

    def split(number: str, to_split: str) -> str:
        nb = int(to_split)
        return number.replace(to_split, f"[{nb // 2},{(nb+1)//2}]", 1)

    def reduce(number: str) -> str:
        while True:
            nb_brackets = 0
            for i, c in enumerate(number):
                if c == "[":
                    nb_brackets += 1
                if c == "]":
                    nb_brackets -= 1
                if (
                    nb_brackets > 4
                    and re.search(r"^\[\d+,\d+\]", number[i:]) is not None
                ):
                    number = explode(number, i)
                    break
            else:
                all_numbers = (
                    number.replace("[", " ").replace("]", " ").replace(",", " ").split()
                )
                for nb in iter(all_numbers):
                    if len(nb) > 1:
                        number = split(number, nb)
                        break
                else:
                    return number

    def magnitude(acc: list[Any] | int) -> int:
        if isinstance(acc, int):
            return acc
        return 3 * magnitude(acc[0]) + 2 * magnitude(acc[1])

    acc = ""
    for number in input_data:
        acc = f"[{acc},{number}]" if acc else number
        acc = reduce(acc)
    return magnitude(eval(acc))


def part_2(input_data):
    def explode_replace(number: str, to_add: int, reverse: bool):
        if reverse:
            number = number[::-1]
        match = re.search(r"\d+", number)
        if match is None:
            return number[::-1] if reverse else number
        matched = number[match.start() : match.end()]
        replace_value = (
            str(int(matched[::-1]) + to_add)[::-1]
            if reverse
            else str(int(matched) + to_add)
        )
        replaced = (
            number.replace(matched, replace_value, 1)[::-1]
            if reverse
            else number.replace(matched, replace_value, 1)
        )
        return replaced

    @lru_cache(maxsize=100000)
    def explode(number: str, i: int) -> str:
        match = re.search(r"^\[(\d+),(\d+)\]", number[i:])
        if match is None:
            raise ValueError(number[i:])
        left = explode_replace(number[:i], int(match.groups()[0]), True)
        right = explode_replace(
            number[match.end() + i :], int(match.groups()[1]), False
        )
        return f"{left}0{right}"

    @lru_cache(maxsize=100000)
    def split(number: str, to_split: str) -> str:
        nb = int(to_split)
        return number.replace(to_split, f"[{nb // 2},{(nb+1)//2}]", 1)

    @lru_cache(maxsize=100000)
    def reduce(number: str) -> str:
        while True:
            nb_brackets = 0
            for i, c in enumerate(number):
                if c == "[":
                    nb_brackets += 1
                if c == "]":
                    nb_brackets -= 1
                if (
                    nb_brackets > 4
                    and re.search(r"^\[\d+,\d+\]", number[i:]) is not None
                ):
                    number = explode(number, i)
                    break
            else:
                all_numbers = (
                    number.replace("[", " ").replace("]", " ").replace(",", " ").split()
                )
                for nb in all_numbers:
                    if len(nb) > 1:
                        number = split(number, nb)
                        break
                else:
                    return number

    def magnitude(acc: list[Any] | int) -> int:
        if isinstance(acc, int):
            return acc
        return 3 * magnitude(acc[0]) + 2 * magnitude(acc[1])

    numbers = list(input_data)
    return max(
        magnitude(eval(reduce(f"[{n1},{n2}]")))
        for i, n1 in enumerate(numbers)
        for j, n2 in enumerate(numbers)
        if i != j
    )
