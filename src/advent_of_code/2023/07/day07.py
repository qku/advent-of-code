CARD_LABELS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARD_LABELS_J = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
def map_to_numbers(hand: str, joker: bool = False) -> list[int]:
    if joker:
        return [CARD_LABELS_J.index(card) for card in hand]
    else:
        return [CARD_LABELS.index(card) for card in hand]


def hand_type(hand: str, joker: bool = False) -> int:
    if joker:
        jokers = hand.count('J')
        if jokers == 5:
            # special case: 'JJJJJ'
            return 6
        hand = hand.replace('J', '')
    else:
        jokers = 0
    occurrences = [hand.count(i) for i in set(hand)]
    occurrences.sort(reverse=True)
    if occurrences[0] + jokers == 5:
        # five of a kind
        return 6
    if occurrences[0] + jokers == 4:
        # four of a kind
        return 5
    if occurrences[0] + occurrences[1] + jokers == 5:
        # full house
        return 4
    if occurrences[0] + jokers == 3:
        # three of a kind
        return 3
    if occurrences[0] + occurrences[1] + jokers == 4:
        # two pair
        return 2
    if occurrences[0] + jokers == 2:
        # one pair
        return 1
    return 0


def get_key(joker: bool = False) -> callable:
    def key(hand_bid: tuple[str, int]) -> tuple[int, ...]:
        hand, bid = hand_bid
        keys = [hand_type(hand, joker=joker)]
        keys += map_to_numbers(hand, joker=joker)
        return tuple(keys)
    return key


def total_winnings(hands: list[tuple[str, int]], joker: bool = False) -> int:
    hands.sort(key=get_key(joker=joker))
    tot = 0
    rank = 1
    for hand, bid in hands:
        tot += rank * bid
        rank += 1
    return tot


def read_input(input_file: str) -> list[tuple[str, int]]:
    hands = []
    with open(input_file) as f:
        for line in f.readlines():
            splits = line.split()
            hands.append((splits[0], int(splits[1])))
    return hands


def part_1(input_file: str) -> int:
    hands = read_input(input_file)
    return total_winnings(hands)


def part_2(input_file: str) -> int:
    hands = read_input(input_file)
    return total_winnings(hands, joker=True)


if __name__ == '__main__':
    solution_part_1 = part_1('input.txt')
    print(f'Solution to part 1: {solution_part_1}')

    solution_part_2 = part_2('input.txt')
    print(f'Solution to part 2: {solution_part_2}')
