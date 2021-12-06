from advent_2020.helpers import get_input


def seat_id(seat: str) -> int:
    base_2_seat = (
        seat.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    )
    return int(base_2_seat[:7], 2) * 8 + int(base_2_seat[7:], 2)


if __name__ == "__main__":
    print(max(seat_id(seat) for seat in get_input()))
