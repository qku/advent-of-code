from itertools import cycle


def read_input(f):
    with open(f) as file:
        lines = file.readlines()
    return [int(line.split(':')[1]) for line in lines]


def move(old_pos, roll):
    new_pos = (old_pos + roll) % 10
    if new_pos == 0:
        return 10
    else:
        return new_pos


def fresh_det_die():
    return list(range(1, 101))[::-1]


def deterministic_game(f):
    pos = read_input(f)
    score = [0, 0]
    turn = cycle([0, 1])
    vic_score = 1000
    die = fresh_det_die()
    roll_counter = 0

    while score[0] < vic_score and score[1] < vic_score:
        p = next(turn)
        roll = 0
        for i in range(3):
            if not die:
                die = fresh_det_die()
            roll += die.pop()
            roll_counter += 1

        new_pos = move(pos[p], roll)
        pos[p] = new_pos
        score[p] += new_pos
        print(f'Roll: {roll_counter:4d} P1: {score[0]:4d} P2: {score[1]:4d}')

    losing_score = score[int(not p)]
    return losing_score * roll_counter


if __name__ == '__main__':
    part_1 = deterministic_game('input.txt')
    print(f'Solution to part I: {part_1}')

