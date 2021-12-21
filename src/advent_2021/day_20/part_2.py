from advent_2021.helpers import get_input


if __name__ == "__main__":
    input_getter = get_input()
    enhancer = ""
    image: list[str] = []
    for line in input_getter:
        if line == "":
            break
        enhancer += line
    for line in input_getter:
        image.append(f"{'.'* 54}{line}{'.'* 54}")
    image = ["." * len(image[0])] * 54 + image + ["." * len(image[0])] * 54

    for _ in range(50):
        next_image: list[str] = []
        for y, line in enumerate(image[1:-1], start=1):
            next_line = ""
            for x, c in enumerate(line[1:-1], start=1):
                pixels = (
                    image[y - 1][x - 1 : x + 2]
                    + image[y][x - 1 : x + 2]
                    + image[y + 1][x - 1 : x + 2]
                )
                index = int(pixels.replace(".", "0").replace("#", "1"), 2)
                next_line += enhancer[index]
            next_image.append(f"{next_line[0]}{next_line}{next_line[0]}")
        next_image = [next_image[0]] + next_image + [next_image[0]]

        image = next_image

    print(sum(line.count("#") for line in image))
