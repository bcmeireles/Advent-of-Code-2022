with open("Day 7/input.in", "r") as f:
    data = [x.split() for x in f.readlines()]

current_size = 0

dir_sum = {"/": 0}
fs = {"/": {
    "in": [],
    "parent": "/"
}}
current_dir = "/"
read_files = []

for line in data:
    if line[1] == "cd":
        if line[2] == "..":
            current_dir = fs[current_dir]["parent"]
        else:
            priv_dir = current_dir
            current_dir += line[2] + "/"
            fs[priv_dir]["in"].append(current_dir) if current_dir != "/" else None
        if current_dir not in dir_sum:
            dir_sum[current_dir] = 0
        if current_dir not in fs:
            fs[current_dir] = {
                "in": [],
                "parent": priv_dir
            }

    elif line[1] == "dir":
        fs[current_dir].append(line[2] + "/")
        if line[1] not in dir_sum:
            dir_sum[line[2]] = 0
        if line[1] not in fs:
            fs[line[2]] = []

    elif line[0].isnumeric():
        dir_sum[current_dir] += int(line[0])
        if current_dir != "/":
            parent = fs[current_dir]["parent"]
            while parent != "/":
                dir_sum[parent] += int(line[0])
                parent = fs[parent]["parent"]
            dir_sum["/"] += int(line[0])

sum_ = 0

for value in dir_sum.values():
    sum_ += value if value <= 100000 else 0

print(sum_)