from advent_2021.helpers import get_input


def fold(dots: set[tuple[int, int]], fold_dir: str, fold_coord: int):
    if fold_dir == "x":
        return {
            (x, y) if x < fold_coord else (2 * fold_coord - x, y)
            for x, y in dots
            if x != fold_coord
        }
    return {
        (x, y) if y < fold_coord else (x, 2 * fold_coord - y)
        for x, y in dots
        if y != fold_coord
    }


if __name__ == "__main__":
    dots: set[tuple[int, int]] = set()
    input_getter = get_input()
    for line in input_getter:
        if len(line) == 0:
            break
        x, y = line.split(",")
        dots.add((int(x), int(y)))

    for fold_instruction in input_getter:
        fold_dir = fold_instruction[11]
        fold_coord = int(fold_instruction[13:])
        dots = fold(dots, fold_dir, fold_coord)
        break

    print(len(dots))
