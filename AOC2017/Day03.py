my_value = 277678
corner_list = [1]
total = 1
increment = 2
position_list = ["center"]
corner_dict = {0: "UR", 1: "UL", 2: "DL", 3: "DR"}

while total <= my_value:
    for i in range(4):
        total += increment
        corner_list.append(total)
        position_list.append(corner_dict[i])
    increment += 2

master_list = list(zip(corner_list, position_list))
# print(master_list)
corner1 = master_list[-2]
corner2 = master_list[-1]
count = 0
x = 0
print(corner1, corner2)

if "D" in corner1[1] and "D" in corner2[1]:
    x = my_value - abs((corner2[0] - corner1[0]))
if "U" in corner1[1] and "U" in corner2[1]:
    x = my_value - abs(corner2[0] - corner1[0])
if "L" in corner1[1] and "L" in corner2[1]:
    x = my_value - abs(corner2[0] - corner1[0])
if "R" in corner1[1] and "R" in corner2[1]:
    x = my_value - abs(corner2[0] - corner1[0])

if abs(corner1[0] - my_value) < abs(corner2[0] - my_value):
    nearest_corner = corner1
else:
    nearest_corner = corner2

for corner in master_list:
    if corner[1] == nearest_corner[1]:
        count += 1

print(x, count)
print(abs(x) + count)
