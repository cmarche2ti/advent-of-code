puzzle = []
radii = []

test = """pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1"""

# for line in test.split("\n"):
#     radii.append(int(line.split("=")[2]))
#     puzzle.append(line.split("=")[1][:-3])

with open("data/Day23.txt", "r") as f:
    for line in f:
        radii.append(int(line.split("=")[2]))
        puzzle.append(line.split("=")[1][:-3])

max_radii = max(radii)
max_index = radii.index(max(radii))
max_pos = puzzle[max_index]
x, y, z = max_pos.split(",")
x = int(x[1:])
y = int(y)
z = int(z[:-1])
print(x, y, z, max(radii))

in_range = 0
for val in puzzle:
    temp = val.replace(">", "").replace("<", "")
    pos = temp.split(",")
    sum = abs(int(pos[0]) - x) + abs(int(pos[1]) - y) + abs(int(pos[2]) - z)
    if sum <= max_radii:
        print(val)
        in_range += 1

print(in_range)

