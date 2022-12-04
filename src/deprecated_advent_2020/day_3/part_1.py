from advent_2020.helpers import get_input


if __name__ == "__main__":
    data = list(get_input())
    tree_count = 0
    for j in range(len(data)):
        tree_count += data[j][3 * j % len(data[0])] == "#"
    print(tree_count)
