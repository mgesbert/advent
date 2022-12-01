from advent_2022.helpers import get_input


if __name__ == "__main__":
    print(
        max(
            sum(int(calories) for calories in elve_carry.split("|"))
            for elve_carry in "|".join(get_input()).split("||")
        )
    )
