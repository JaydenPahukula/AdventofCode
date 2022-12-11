
def solution():
    score = 0
    with open("day02/input.txt", "r") as file:
        data = [x.replace('\n','').split(' ') for x in file.readlines()]

    pts = {'X':0,'Y':3,'Z':6}

    for a, b in data:
        roundscore = pts[b]
        if a == 'A':
            if b == 'X':
                roundscore += 3
            elif b == 'Y':
                roundscore += 1
            else:
                roundscore += 2
        elif a == 'B':
            if b == 'X':
                roundscore += 1
            elif b == 'Y':
                roundscore += 2
            else:
                roundscore += 3
        else:
            if b == 'X':
                roundscore += 2
            elif b == 'Y':
                roundscore += 3
            else:
                roundscore += 1
        score += roundscore

    return score


print(solution())