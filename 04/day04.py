import numpy as np


def read_bingo_data(f):
    d = np.loadtxt(f, delimiter=',', max_rows=1, dtype=int)
    b_array = np.loadtxt(f, skiprows=2, dtype=int)
    b_list = [b_array[i:i+5] for i in range(0, b_array.shape[0], 5)]
    return d, b_list


def single_draw(d, b):
    """ Set matching numbers on board to -1 """
    b[b == d] = -1


def check_victory(b):
    column_victory = (b.sum(axis=0) == -5).any()
    row_victory = (b.sum(axis=1) == -5).any()
    return column_victory or row_victory


def calculate_score(b, last_draw):
    unmarked = b[b != -1]
    return unmarked.sum() * last_draw


def play_bingo(d_array, b_list):
    for d in d_array:
        for b in b_list:
            single_draw(d, b)
            if check_victory(b):
                return calculate_score(b, d)


def find_last_winning(d_array, b_list):
    losers = b_list
    for d in d_array:
        for b in losers:
            single_draw(d, b)

        old_losers = losers
        losers = []
        for b in old_losers:
            if not check_victory(b):
                losers.append(b)

        if len(losers) == 0:
            return calculate_score(old_losers[0], d)


def test_play():
    assert play_bingo(test_draws, test_boards) == 4512


def test_read():
    second_board_first_row = np.array([3, 15, 0, 2, 22])
    assert (test_boards[1][0] == second_board_first_row).all()


def test_last():
    assert find_last_winning(test_draws, test_boards) == 1924


draws, boards = read_bingo_data('input.txt')
test_draws, test_boards = read_bingo_data('test_input.txt')

final_score = play_bingo(draws, boards)
final_score_last = find_last_winning(draws, boards)
print(f'Score: {final_score}')
print(f'Score of last winning: {final_score_last}')
