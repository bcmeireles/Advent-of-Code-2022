with open("Day 2/input.in", "r") as f:
    data = f.readlines()

scoring = 0

my_outcomes_scoring = {
    "X": 1, # rock
    "Y": 2, # paper
    "Z": 3 # scissors
}

my_win_conditions = {
    "A": "Y", # rock
    "B": "Z", # paper
    "C": "X" # scissor
}

my_loss_conditions = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

draw_conditions = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

for line in data:
    if line[2] == "X": # need to lose
        my_play = my_loss_conditions[line[0]]
    elif line[2] == "Y": # need to draw
        my_play = draw_conditions[line[0]]
        scoring += 3
    elif line[2] == "Z": # need to win
        my_play = my_win_conditions[line[0]]
        scoring += 6

    scoring += my_outcomes_scoring[my_play]

print(scoring)