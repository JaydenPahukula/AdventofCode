
def solution():
    score = 0
    with open("day02/input.txt", "r") as file:
        data = [x.replace('\n','').split(' ') for x in file.readlines()]

    pts = {'X':1,'Y':2,'Z':3}

    for a, b in data:
        roundscore = pts[b]
        if a == 'A':
            if b == 'X':
                roundscore += 3
            elif b == 'Y':
                roundscore += 6
        elif a == 'B':
            if b == 'Y':
                roundscore += 3
            elif b == 'Z':
                roundscore += 6
        else:
            if b == 'Z':
                roundscore += 3
            elif b == 'X':
                roundscore += 6
        score += roundscore

    return score


print(solution())