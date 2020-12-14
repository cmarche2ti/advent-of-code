puzzle = """16
10
15
5
1
11
7
19
6
12
4"""

puzzle = puzzle.split("\n")
# puzzle = []
# with open("data/Day10.txt", "r") as f:
#     for line in f:
#         puzzle.append(line[:-1])

puzzle = sorted([int(p) for p in puzzle])
print(puzzle)

# part 1
one = 1
three = 1
for i in range(1, len(puzzle)):
    if puzzle[i] - puzzle[i - 1] == 3:
        three += 1
    elif puzzle[i] - puzzle[i - 1] == 1:
        one += 1

print(one, three, one * three)

# part 2

