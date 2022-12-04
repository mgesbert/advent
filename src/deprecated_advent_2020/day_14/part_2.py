import re
import sys

from advent_2020.helpers import get_input


def floating_addresses(address: str, acc: list[str] | None = None) -> list[str]:
    if acc is None:
        acc = [""]
    if len(address) == 0:
        return acc
    if address[0] != "X":
        return floating_addresses(address[1:], [a + address[0] for a in acc])
    return floating_addresses(address[1:], [a + i for a in acc for i in "01"])


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
        bin_index = f"{int(index):b}".zfill(36)
        masked_index = "".join(
            c if c != "0" else bin_index[i] for i, c in enumerate(mask)
        )

        for address in floating_addresses(masked_index):
            mem[int(address, 2)] = int(value)

    print(sum(mem.values()))
