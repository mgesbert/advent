import re

with open("src/2022/data/day_21.txt") as f:
    instructions = [
        "def " + re.sub(r"([a-zA-Z]+)", r"\1()", line).replace(":", ": return")
        for line in f.readlines()
    ]

exec("".join(instructions))
print(int(root()))  # type: ignore # noqa: F821
