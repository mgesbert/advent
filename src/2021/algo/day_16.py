TRANSLATION = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def part_1(input_data):
    def parse_operator(data: str, acc: int = 0):
        version = int(data[:3], 2)
        acc += version
        type_id = int(data[3:6], 2)

        data = data[6:]
        if type_id == 4:
            while data.startswith("1"):
                data = data[5:]
            data = data[5:]
        else:
            length_type_id = int(data[0])
            data = data[1:]
            if length_type_id == 0:
                sub_data_length = int(data[:15], 2)
                data = data[15:]
                sub_data = data[:sub_data_length]
                data = data[sub_data_length:]
                while any(c != "0" for c in sub_data):
                    sub_data, acc = parse_operator(sub_data, acc)
            else:
                nb_packets = int(data[:11], 2)
                data = data[11:]
                for _ in range(nb_packets):
                    data, acc = parse_operator(data, acc)
        return data, acc

    data = next(input_data)
    data = "".join([TRANSLATION[c] for c in data])
    _, result = parse_operator(data)
    return result


def part_2(input_data):
    def product(args: tuple[int, ...]) -> int:
        if len(args) == 0:
            return 1
        return args[0] * product(args[1:])

    def gt(l: tuple[int, int]):
        a, b = l
        return int(a > b)

    def lt(l: tuple[int, int]):
        a, b = l
        return int(a < b)

    def eq(l: tuple[int, int]):
        a, b = l
        return int(a == b)

    OPERATORS = {
        0: sum,
        1: product,
        2: min,
        3: max,
        5: gt,
        6: lt,
        7: eq,
    }

    def parse_operator(data: str) -> tuple[int, str]:
        type_id = int(data[3:6], 2)
        data = data[6:]

        if type_id == 4:
            value = 0
            while True:
                value *= 16
                value += int(data[1:5], 2)
                if data.startswith("0"):
                    data = data[5:]
                    break
                data = data[5:]
            return value, data

        length_type_id = int(data[0])
        data = data[1:]
        sub_values: list[int] = []

        if length_type_id == 0:
            sub_data_length = int(data[:15], 2)
            data = data[15:]
            sub_data = data[:sub_data_length]
            data = data[sub_data_length:]
            while any(c != "0" for c in sub_data):
                sub_value, sub_data = parse_operator(sub_data)
                sub_values.append(sub_value)

        else:
            nb_packets = int(data[:11], 2)
            data = data[11:]
            for _ in range(nb_packets):
                value, data = parse_operator(data)
                sub_values.append(value)

        value: int = OPERATORS[type_id](sub_values)  # type: ignore
        return value, data

    data = next(input_data)
    data = "".join([TRANSLATION[c] for c in data])
    result, _ = parse_operator(data)
    return result
