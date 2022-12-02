with open("Day 1/2.in", "r") as f:
    data = f.readlines()

elf_carries = 0
max_carriers = [0, 0, 0]

def check():
    global elf_carries
    global max_carriers

    if elf_carries > max_carriers[0]:
        max_carriers[2] = max_carriers[1]
        max_carriers[1] = max_carriers[0]
        max_carriers[0] = elf_carries
    elif elf_carries > max_carriers[1]:
        max_carriers[2] = max_carriers[1]
        max_carriers[1] = elf_carries
    elif elf_carries > max_carriers[2]:
        max_carriers[2] = elf_carries
    elf_carries = 0

for line in data:
    if line == "\n":
        check()
    else:
        elf_carries += int(line)
check()

print(sum(max_carriers))