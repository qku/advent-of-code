CARD_LABELS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
def map_to_numbers(hand: str) -> list[int]:
    return [CARD_LABELS.index(card) for card in hand]


def hand_type(hand: str) -> int:
    hand = map_to_numbers(hand)
    occurrences = [hand.count(i) for i in set(hand)]
    if 5 in occurrences:
        # five of a kind
        return 6
    if 4 in occurrences:
        # four of a kind
        return 5
    if 3 in occurrences and 2 in occurrences:
        # full house
        return 4
    if 3 in occurrences:
        # three of a kind
        return 3
    if occurrences.count(2) == 2:
        # two pair
        return 2
    if 2 in occurrences:
        # one pair
        return 1
    return 0


def key(hand_bid: tuple[str, int]) -> tuple[int, ...]:
    hand, bid = hand_bid
    keys = [hand_type(hand)]
    keys += map_to_numbers(hand)
    return tuple(keys)


def part_1(input_file: str) -> int:
    hands: list[tuple[str, int]] = []
    with open(input_file) as f:
        for line in f.readlines():
            splits = line.split()
            hands.append((splits[0], int(splits[1])))
    hands.sort(key=key)
    total_winnings = 0
    rank = 1
    for hand, bid in hands:
        total_winnings += rank * bid
        rank += 1
    return total_winnings


def part_2(input_file: str) -> int:
    return 0


if __name__ == '__main__':
    solution_part_1 = part_1('input.txt')
    print(f'Solution to part 1: {solution_part_1}')

    solution_part_2 = part_2('input.txt')
    print(f'Solution to part 2: {solution_part_2}')
