with open('input.txt') as f:
    turns = f.readlines()

opp_choice, your_choice = [], []
for turn in turns:
    choices = turn.split()

    opp_choice.append(ord(choices[0]) - 64)
    your_choice.append(ord(choices[1]) - 87)

# part 1
score = 0
for opp, you in zip(opp_choice, your_choice):
    score += you

    winner = (opp - you) % 3

    if winner == 0:
        score += 3
    elif winner == 2:
        score += 6

print(score)

# part 2
score = 0
for opp, you in zip(opp_choice, your_choice):
    if you == 2:
        # draw
        score += 3
        guide_choice = opp
    elif you == 3:
        # win
        score += 6
        guide_choice = (opp % 3) + 1
    else:
        # lose
        guide_choice = ((opp - 2) % 3) + 1
    score += guide_choice

print(score)
