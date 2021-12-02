data = []
with open("data/Day02.txt", "r") as f:
    for line in f:
        data.append(line.strip().split(" "))

test_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

test_data = [val.strip().split(" ") for val in test_data.split("\n")]

# part 1
def postion_product(l):
    horiz = 0
    vert = 0
    for val in l:
        if val[0] == "up":
            vert -= int(val[1])
        elif val[0] == "down":
            vert += int(val[1])
        else:
            horiz += int(val[1])
    print(horiz, vert, horiz * vert)


postion_product(test_data)
postion_product(data)

# part 2
def postion_product_aim(l):
    horiz = 0
    depth = 0
    aim = 0
    for val in l:
        if val[0] == "up":
            aim -= int(val[1])
        elif val[0] == "down":
            aim += int(val[1])
        else:
            horiz += int(val[1])
            depth += aim * int(val[1])
    print(horiz, depth, aim, horiz * depth)


postion_product_aim(test_data)
postion_product_aim(data)
