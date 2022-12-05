with open("Day 5/input.in", "r") as f:
    data = f.readlines()

for line in data:
    if line[1].isnumeric():
        box_count = int(line[-3])
        arrangement_last_line = data.index(line)
        break

boxes = []

for _ in range(box_count):
    boxes.append([])

for i in range(arrangement_last_line):
    line = data[i]
    box = 0
    j = 1
    while box < box_count:
        if line[j] != " ":
            boxes[box].append(line[j]) 
        box += 1
        j += 4

for box in boxes:
    box.reverse()


for line in data[arrangement_last_line + 2:]:
    amount = int(line[line.find("move ")+len("move "):line.rfind(" from")])
    box_from = int(line[line.find(" from ")+len(" from "):line.rfind(" to ")])
    box_to = int(line[line.find(" to ")+len(" to ")])

    for _ in range(amount):
        boxes[box_to - 1].append(boxes[box_from - 1].pop())

code = ""
for box in boxes:
    code += box[-1]

print(code)