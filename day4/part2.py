
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

        for x in range(int(b[0]), int(b[1])+1):
            if x in first:
                score += 1
                break


    return score


print(solution())