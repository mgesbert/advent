import re
import sys

from advent_2020.helpers import get_input


if __name__ == "__main__":
    mem: dict[int, int] = {}
    mask = ""
    for line in get_input():
        if "mask" in line:
            mask = line.split(" = ")[1]
            continue
        search_result = re.search(r"mem\[(\d+)\] = (\d+)$", line)
        if search_result is None:
            sys.exit(1)
        index, value = search_result.groups()
        bin_value = f"{int(value):b}".zfill(36)
        masked_value = "".join(
            c if c != "X" else bin_value[i] for i, c in enumerate(mask)
        )
        mem[int(index)] = int(masked_value, 2)
    print(sum(mem.values()))
