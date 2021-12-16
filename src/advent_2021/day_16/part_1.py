from advent_2021.helpers import get_input


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


if __name__ == "__main__":
    data = next(get_input())
    data = "".join([TRANSLATION[c] for c in data])
    _, result = parse_operator(data)
    print(result)
