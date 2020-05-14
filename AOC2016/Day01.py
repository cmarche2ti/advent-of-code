import collections as col

puzzle = "R4, R3, L3, L2, L1, R1, L1, R2, R3, L5, L5, R4, L4, R2, R4, L3, R3, L3, R3, R4, R2, L1, R2, L3, L2, L1, R3, R5, L1, L4, R2, L4, R3, R1, R2, L5, R2, L189, R5, L5, R52, R3, L1, R4, R5, R1, R4, L1, L3, R2, L2, L3, R4, R3, L2, L5, R4, R5, L2, R2, L1, L3, R3, L4, R4, R5, L1, L1, R3, L5, L2, R76, R2, R2, L1, L3, R189, L3, L4, L1, L3, R5, R4, L1, R1, L1, L1, R2, L4, R2, L5, L5, L5, R2, L4, L5, R4, R4, R5, L5, R3, L1, L3, L1, L1, L3, L4, R5, L3, R5, R3, R3, L5, L5, R3, R4, L3, R3, R1, R3, R2, R2, L1, R1, L3, L3, L3, L1, R2, L1, R4, R4, L1, L1, R3, R3, R4, R1, L5, L2, R2, R3, R2, L3, R4, L5, R1, R4, R5, R4, L4, R1, L3, R1, R3, L2, L3, R1, L2, R3, L3, L1, L3, R4, L4, L5, R3, R5, R4, R1, L2, R3, R5, L5, L4, L1, L1"
puzzle = puzzle.split(", ")
direction = col.deque("NESW")
x, y = 0, 0
all_positions = set()
first_position_twice = ()
for p in puzzle:
    if "R" in p:
        direction.rotate()
    else:
        direction.rotate(-1)
    if direction[0] == "N":
        y += int(p.replace(p[0], ""))
    elif direction[0] == "S":
        y -= int(p.replace(p[0], ""))
    elif direction[0] == "E":
        x += int(p.replace(p[0], ""))
    elif direction[0] == "W":
        x -= int(p.replace(p[0], ""))
    position = (x, y)
    if position in all_positions:
        first_position_twice = position
    else:
        all_positions.add((x, y))

print("Part 1 answer:")
print(abs(x) + abs(y))
print("Part 2 answer:")
print(first_position_twice)
print(abs(first_position_twice[0]) + abs(first_position_twice[1]))
