from collections import defaultdict

CARD_VALUES = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
}

HAND_TYPES = [
    [1, 1, 1, 1, 1],
    [2, 1, 1, 1],
    [2, 2, 1],
    [3, 1, 1],
    [3, 2],
    [4, 1],
    [5],
]


def card_value(card):
    if card in CARD_VALUES:
        return CARD_VALUES[card]
    return int(card)


def hand_value(hand, joker_value=None):
    occurences = defaultdict(int)
    for card in hand:
        occurences[joker_value if joker_value and card == "J" else card] += 1
    card_groups = sorted(occurences.values(), reverse=True)

    return (
        HAND_TYPES.index(card_groups),
        *(card_value("1" if joker_value and card == "J" else card) for card in hand),
    )


def part_1(input_data):
    game = [(hand, int(bid)) for hand, bid in [line.split() for line in input_data]]
    bids = [bid for _, bid in sorted(game, key=lambda x: hand_value(x[0]))]
    return sum(bid * i for i, bid in enumerate(bids, start=1))


def hand_value_with_joker(hand):
    return max(hand_value(hand, joker_value=card) for card in set(hand) - {"J"} | {"A"})


def part_2(input_data):
    game = [(hand, int(bid)) for hand, bid in [line.split() for line in input_data]]
    bids = [bid for _, bid in sorted(game, key=lambda x: hand_value_with_joker(x[0]))]
    return sum(bid * i for i, bid in enumerate(bids, start=1))
