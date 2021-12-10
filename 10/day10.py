closing = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def find_first_illegal_in_line(line):
    opened_brackets = []
    for k in line:
        if k in '([{<':
            opened_brackets.append(k)
        elif closing[opened_brackets[-1]] == k:
            del opened_brackets[-1]
        else:
            return k
    return opened_brackets


score_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def score_syntax_error(f):
    score = 0
    with open(f) as file:
        for i in file:
            if i.isspace():
                continue
            i = i.strip()
            res = find_first_illegal_in_line(i)
            if len(res) == 1:
                score += score_table[find_first_illegal_in_line(i)]
    return score


auto_score_table = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def autocomplete(f):
    scores = []
    with open(f) as file:
        for i in file:
            if i.isspace():
                continue
            i = i.strip()
            res = find_first_illegal_in_line(i)
            if len(res) == 1:
                continue

            closing_brackets = [closing[i] for i in res[::-1]]

            line_score = 0
            for b in closing_brackets:
                line_score *= 5
                line_score += auto_score_table[b]
            scores.append(line_score)
    n = len(scores)
    scores.sort()
    return scores[int((n-1) / 2)]


final_score = score_syntax_error('input.txt')
print(f'Syntax error score: {final_score}')
final_score_auto = autocomplete('input.txt')
print(f'Autocomplete score: {final_score_auto}')




