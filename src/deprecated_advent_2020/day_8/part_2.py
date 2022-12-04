from advent_2020.helpers import get_input


def backtracking(
    stack: list[tuple[str, int]], i: int, acc: int, visited: set[int], switched: bool
) -> bool:
    if i in visited:
        return False
    new_visited: set[int] = set(visited) | {i}
    ins, value = stack[i]
    if ins == "nop":
        i += 1
    elif ins == "acc":
        acc += value
        i += 1
    elif ins == "jmp":
        i += value
    if i >= len(stack):
        print(acc)
        return True
    if backtracking(stack, i, acc, new_visited, switched):
        return True
    next_ins, next_value = stack[i]
    if not switched and next_ins in ["jmp", "nop"]:
        new_stack = [*stack]
        new_stack[i] = (["jmp", "nop"][next_ins == "jmp"], next_value)
        return backtracking(new_stack, i, acc, new_visited, True)
    return False


if __name__ == "__main__":
    stack: list[tuple[str, int]] = []
    for line in get_input():
        ins, value = line.split()
        stack.append((ins, int(value)))

    backtracking(stack, 0, 0, set(), False)
