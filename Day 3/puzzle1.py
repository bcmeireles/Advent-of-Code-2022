with open("Day 3/input.in", "r") as f:
    data = f.readlines()

def getSame(s1, s2, s3):
    for l in s1:
        if l in s2 and l in s3:
            return l

def getValue(l):
    if l.islower():
        return ord(l) - 96
    else:
        return ord(l) - 38
    
sum = 0
i = 0

while i + 2 < len(data):
    sum += getValue(getSame(data[i], data[i + 1], data[i + 2]))
    i += 3

print(sum)