from advent_2020.helpers import get_input


def neighbors(seats: list[str], i: int, j: int) -> str:
    h = len(seats)
    w = len(seats[0])
    result = ""

    for x_dir in [-1, 0, 1]:
        for y_dir in [-1, 0, 1]:
            if x_dir == y_dir == 0:
                continue

            x, y = i + x_dir, j + y_dir
            while 0 <= x < w and 0 <= y < h and seats[y][x] == ".":
                x += x_dir
                y += y_dir
            if 0 <= x < w and 0 <= y < h:
                result += seats[y][x]

    return result


if __name__ == "__main__":
    seats: list[str] = []
    next_seats = list(get_input())
    while seats != next_seats:
        seats = next_seats
        next_seats = [
            "".join(
                "."
                if seat == "."
                else "#"
                if seat == "#"
                and sum(s == "#" for s in neighbors(seats, i, j)) < 5
                or seat == "L"
                and sum(s == "#" for s in neighbors(seats, i, j)) == 0
                else "L"
                for i, seat in enumerate(seats[j])
            )
            for j in range(len(seats))
        ]
    print(sum(row.count("#") for row in seats))
