from advent_2020.helpers import get_input


def neighbors(seats: list[str], i: int, j: int) -> str:
    result = ""

    if j > 0:
        if i > 0:
            result += seats[j - 1][i - 1]
        result += seats[j - 1][i]
        if i + 1 < len(seats[0]):
            result += seats[j - 1][i + 1]
    if i > 0:
        result += seats[j][i - 1]
    if i + 1 < len(seats[0]):
        result += seats[j][i + 1]
    if j + 1 < len(seats):
        if i > 0:
            result += seats[j + 1][i - 1]
        result += seats[j + 1][i]
        if i + 1 < len(seats[0]):
            result += seats[j + 1][i + 1]

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
                and sum(s == "#" for s in neighbors(seats, i, j)) < 4
                or seat == "L"
                and sum(s == "#" for s in neighbors(seats, i, j)) == 0
                else "L"
                for i, seat in enumerate(seats[j])
            )
            for j in range(len(seats))
        ]
    print(sum(row.count("#") for row in seats))
