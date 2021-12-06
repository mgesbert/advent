import sys

from advent_2021.helpers import get_input


digits = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


if __name__ == "__main__":
    # print(
    #     sum(
    #         len(digit) in [2, 3, 4, 7]
    #         for line in get_input()
    #         for digit in line.split(" | ")[1].split()
    #     )
    # )
    result = 0
    for line in get_input():
        signal = line.split(" | ")[0].split()
        output = line.split(" | ")[1].split()
        mapping = {d: list("abcdefg") for d in "abcdefg"}

        one = next(s for s in signal if len(s) == 2)
        for x in "cf":
            mapping[x] = list(one)

        seven = next(s for s in signal if len(s) == 3)
        mapping["a"] = list(set(seven) - set(one))

        six_nine_zero = [s for s in signal if len(s) == 6]
        for s in six_nine_zero:
            c = next((x for x in mapping["c"] if x not in s), None)
            if c is not None:
                mapping["f"] = list(set(mapping["c"]) - {c})
                mapping["c"] = [c]

        d_e = [
            y
            for s in six_nine_zero
            for y in next(x for x in "abcdefg" if x not in s)
            if y not in mapping["c"]
        ]
        mapping["d"] = [*d_e]
        mapping["e"] = [*d_e]

        five = next(s for s in signal if len(s) == 5 and mapping["c"][0] not in s)
        mapping["e"] = [next(x for x in mapping["e"] if x not in five)]
        mapping["d"] = [next(x for x in mapping["d"] if x not in mapping["e"])]

        mapping["b"] = [
            x
            for x in "abcdefg"
            if x
            not in mapping["a"]
            + mapping["c"]
            + mapping["d"]
            + mapping["e"]
            + mapping["f"]
        ]
        mapping["g"] = [*mapping["b"]]

        two = next(s for s in signal if len(s) == 5 and mapping["f"][0] not in s)
        mapping["b"] = [next(x for x in mapping["b"] if x not in two)]
        mapping["g"] = [next(x for x in mapping["g"] if x in two)]

        translation = {ord(v[0]): ord(k) for k, v in mapping.items()}
        result += int(
            "".join(digits["".join(sorted(s.translate(translation)))] for s in output)
        )

    print(result)
