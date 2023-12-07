
d = {"2":0,"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,"T":8,"J":-1,"Q":10,"K":11,"A":12}

def strength(s:str):
    # print(s, end=" ")
    cards = [d[c] for c in s]

    jokerStrength = -1
    for i in range(5):
        if s[i] == "J":
            for c in d.keys():
                if c == "J": continue
                jokerStrength = max(jokerStrength, strength(s[:i]+c+s[i+1:]))
            break
    if jokerStrength != -1: return jokerStrength

    sCards = sorted(cards)
    if len(set(cards)) == 1:
        # print("5 of a kind")
        return 6
    c1 = sCards[0]
    c3 = sCards[4]
    if len(set(cards)) == 2:
        if sCards[:4] == [c1,c1,c1,c1] or sCards[1:] == [c3,c3,c3,c3]:
            # print("4 of a kind")
            return 5
        else:
            # print("full house")
            return 4
    c2 = sCards[2]
    if len(set(cards)) == 3:
        if [c2,c2,c2] in (sCards[:3], sCards[1:4], sCards[2:]):
            # print("3 of a kind")
            return 3
        else:
            # print("two pair")
            return 2
    if len(set(cards)) == 4:
        # print("one pair")
        return 1
    else:
        # print("high card")
        return 0


def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    hands = []
    for line in data:
        cards, bid = line.split()
        hand = [strength(cards)]+[d[c] for c in cards]+[int(bid)]
        hands.append(hand)
    
    hands.sort()

    score = 0
    for i in range(len(hands)):
        score += (i+1) * hands[i][-1]
    
    return score


print(solution())