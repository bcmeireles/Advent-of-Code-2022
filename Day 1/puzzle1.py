with open("Day 1/input.in", "r") as f:
    data = f.readlines()

elf_carries = 0
max_carry = 0

def check():
    global elf_carries
    global max_carry

    if elf_carries > max_carry:
        max_carry = elf_carries
    elf_carries = 0

for line in data:
    if line == "\n":
        check()
    else:
        elf_carries += int(line)
check()

print(max_carry)