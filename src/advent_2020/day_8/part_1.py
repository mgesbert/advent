from advent_2020.helpers import get_input


if __name__ == "__main__":
    stack: list[tuple[str, int]] = []
    for line in get_input():
        ins, value = line.split()
        stack.append((ins, int(value)))

    acc = 0
    i = 0
    visited: set[int] = set()

    while i not in visited:
        visited.add(i)
        ins, value = stack[i]
        if ins == "nop":
            i += 1
        elif ins == "acc":
            acc += value
            i += 1
        elif ins == "jmp":
            i += value

    print(acc)
