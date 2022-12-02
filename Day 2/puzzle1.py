with open("Day 2/input.in", "r") as f:
    data = f.readlines()

scoring = 0

my_outcomes_scoring = {
    "X": 1, # rock
    "Y": 2, # paper
    "Z": 3 # scissors
}

my_win_conditions = {
    "X": "C", # scissor
    "Y": "A", # rock
    "Z": "B" # paper
}

draw_conditions = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

for line in data:
    scoring += my_outcomes_scoring[line[2]]
    if draw_conditions[line[2]] == line[0]: # draw
        scoring += 3
    elif line[0] == my_win_conditions[line[2]]: # win
        scoring += 6

print(scoring)