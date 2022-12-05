with open("Day 4/input.in", "r") as f:
    data = f.readlines()

n = 0

for line in data:
    elf1, elf2 = line.split(",")

    elf1min, elf1max = elf1.split("-")
    elf2min, elf2max = elf2.split("-")

    list1 = [x for x in range(int(elf1min), int(elf1max) + 1)]
    list2 = [x for x in range(int(elf2min), int(elf2max) + 1)]

    if any(x in list1 for x in list2):
        n += 1

print(n)