
def solution():

    with open("day4/input.txt", "r") as file:
        data = [x.replace('\n','').split(",") for x in file.readlines() if x != '\n']
    
    score = 0
    for a, b in data:
        a = a.split("-")
        b = b.split("-")

        first = []
        for x in range(int(a[0]),int(a[1])+1):
            first.append(x)

        second = []
        for x in range(int(b[0]), int(b[1])+1):
            second.append(x)
        
        if len(first) < len(second):
            for num in first:
                if num not in second:
                    score -= 1
                    break
            score += 1
        else:
            for num in second:
                if num not in first:
                    score -= 1
                    break
            score += 1

    return score


print(solution())