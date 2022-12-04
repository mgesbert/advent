def part_1(input_data):
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

    dots: set[tuple[int, int]] = set()
    input_getter = input_data
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

    return len(dots)


def part_2(input_data):
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

    dots: set[tuple[int, int]] = set()
    input_getter = input_data
    for line in input_getter:
        if len(line) == 0:
            break
        x, y = line.split(",")
        dots.add((int(x), int(y)))

    for fold_instruction in input_getter:
        fold_dir = fold_instruction[11]
        fold_coord = int(fold_instruction[13:])
        dots = fold(dots, fold_dir, fold_coord)

    return "\n" + "\n".join(
        "".join(
            [
                "#" if (x, y) in dots else " "
                for x in range(min(x for x, _ in dots), max(x for x, _ in dots) + 1)
            ]
        )
        for y in range(min(y for _, y in dots), max(y for _, y in dots) + 1)
    )
