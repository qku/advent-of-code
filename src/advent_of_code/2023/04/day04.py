def count_matching_numbers(input_file: str) -> list[int]:
    res = []
    with open(input_file) as f:
        for card in f.readlines():
            card = card.split(':')[1].strip()
            splits = card.split('|')
            winning, my_numbers = splits[0], splits[1]
            winning = set(winning.split())
            my_numbers = set(my_numbers.split())
            n = len(winning.intersection(my_numbers))
            res.append(n)
    return res


def part_1(input_file: str) -> int:
    score = 0
    card_scores = count_matching_numbers(input_file)
    unscratched_cards = list(range(len(card_scores)))
    while unscratched_cards:
        card = unscratched_cards.pop()
        card_score = card_scores[card]
        if card_score > 0:
            score += 2 ** (card_score - 1)
    return score


def part_2(input_file: str) -> int:
    scratched_cards = 0
    card_scores = count_matching_numbers(input_file)
    unscratched_cards = list(range(len(card_scores)))
    while unscratched_cards:
        card = unscratched_cards.pop()
        scratched_cards += 1
        card_score = card_scores[card]
        for i in range(card_score):
            new_card = card + i + 1
            if new_card < len(card_scores):
                unscratched_cards.append(new_card)
    return scratched_cards


if __name__ == '__main__':
    solution_part_1 = part_1('input.txt')
    print(f'Solution to part 1: {solution_part_1}')

    solution_part_2 = part_2('input.txt')
    print(f'Solution to part 2: {solution_part_2}')
