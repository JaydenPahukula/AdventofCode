
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    copies = [1 for _ in range(len(data))]
    for i, line in enumerate(data):
        line = line.split()
        winning = list(map(int, line[2:12]))
        numWinning = sum([1 if int(x) in winning else 0 for x in line[13:]])
        for j in range(i+1, i+1+numWinning):
            copies[j] += copies[i]

    return sum(copies)


print(solution())