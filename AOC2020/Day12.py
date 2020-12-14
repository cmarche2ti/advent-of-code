import math

puzzle = """F10
N3
F7
R90
F11"""

puzzle = puzzle.split("\n")
puzzle = []

with open("data/Day12.txt", "r") as f:
    for line in f:
        print(line)
        puzzle.append(line.replace("\n", ""))

print(puzzle)
c = {"N": 0, "S": 0, "E": 0, "W": 0}

current = "E"


def turn(direction, d, n):
    turns = int(n) / 90
    compass = "ESWN"
    index = compass.find(direction)
    if d == "R":
        # print(int((index + turns) % 4))
        return compass[int((index + turns) % 4)]
    elif d == "L":
        # print(int((index + turns) % 4))
        return compass[int(4 + (index - turns)) % 4]


for val in puzzle:
    a = val[0]
    b = int(val[1:])
    if val[0] == "R" or val[0] == "L":
        current = turn(current, a, b)
    elif val[0] == "F":
        c[current] += b
    else:
        c[a] += b

print(c)
print(abs(c["N"] - c["S"]) + abs(c["E"] - c["W"]))

# part 2

