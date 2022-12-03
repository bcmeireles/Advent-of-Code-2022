with open("Day 3/input.in", "r") as f:
    data = f.readlines()

def getSame(s1, s2):
    for l in s1:
        if l in s2:
            return l

def getValue(l):
    if l.islower():
        return ord(l) - 96
    else:
        return ord(l) - 38
    
sum = 0

for line in data:
    sum += getValue(getSame(line[:len(line)//2], line[len(line)//2:]))

print(sum)