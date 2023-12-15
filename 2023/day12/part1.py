
def getNums(s:str, target:list):
    for i in range(len(s)):
        if s[i] == "?":
            return getNums(s[:i]+"."+s[i+1:], target) + getNums(s[:i]+"#"+s[i+1:], target)
    return 1 if [len(x) for x in s.split(".") if x] == target else 0

def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    total = 0
    for line in data:
        line = line.split()
        total += getNums(line[0], list(map(int, line[1].split(","))))

    return total


print(solution())