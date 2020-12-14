puzzle = []

with open("data/Day8.txt") as f:
    for line in f:
        puzzle.append(line.replace("\n", ""))

# test puzzle
# puzzle = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6"""
# puzzle = puzzle.split("\n")

# part 1
# instructions = []
# index = 0
# accumulator = 0
# test = True
# while test:
#     if index in instructions:
#         test = False
#     else:
#         instructions.append(index)
#         a, b = puzzle[index].split()
#         if a == "jmp":
#             index += int(b)
#         if a == "nop":
#             index += 1
#         if a == "acc":
#             accumulator += int(b)
#             index += 1

# print(accumulator)

# part 2


def test_puzzle(p):
    instructions = []
    index = 0
    accumulator = 0
    test = True
    while test:
        if index in instructions:
            test = False
        else:
            instructions.append(index)
            a, b = puzzle[index].split()
            if a == "jmp":
                index += int(b)
            if a == "nop":
                index += 1
            if a == "acc":
                accumulator += int(b)
                index += 1
    return (index, accumulator)


x = 0
t = 0
while x != len(puzzle):
    test_p = puzzle.copy()
    if puzzle[t].split()[1] == "nop":
        puzz = "jmp " + puzzle[t].split()[1]
        test_p.insert(t, puzz)
        x, a = test_puzzle(test_p)
    elif puzzle[t].split()[1] == "jmp":
        puzz = "nop " + puzzle[t].split()[1]
        test_p.insert(t, puzz)
        x, a = test_puzzle(test_p)

    t += 1

print(a)
