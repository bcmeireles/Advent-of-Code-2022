with open("Day 6/input.in", "r") as f:
    data = f.readlines()[0]
    
i = 13

while i < len(data):
    chars = [x for x in data[i-13:i +1]]
    for char in chars:
        if chars.count(char) > 1:
            break
    else:
        print(i + 1)
        break
    i += 1