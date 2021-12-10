def matching(a, b):
    if a == '(' and b == ')':
        return True
    elif a == '[' and b == ']':
        return True
    elif a == '{' and b == '}':
        return True
    elif a == '<' and b == '>':
        return True
    else:
        return False


def find_first_illegal_in_line(line):
    opened_brackets = []
    for k in line:
        if k in '([{<':
            opened_brackets.append(k)
        elif matching(opened_brackets[-1], k):
            del opened_brackets[-1]
        else:
            return k


score_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    None: 0
}


def score_syntax_error(f):
    score = 0
    with open(f) as file:
        for i in file:
            if i.isspace():
                continue
            i = i.strip()
            score += score_table[find_first_illegal_in_line(i)]
    return score


final_score = score_syntax_error('input.txt')
print(f'Syntax error score: {final_score}')




