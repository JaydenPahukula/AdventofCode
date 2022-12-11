
def solution():

    with open("day01/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    elves = []
    calories = 0

    for line in data:
        if line == "":
            elves.append(calories)
            calories = 0
        else:
            calories += int(line)
    elves.append(calories)

    elves.sort()
    
    return sum(elves[-3:])


print(solution())