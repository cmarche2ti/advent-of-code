directions = []
lights = []

with open("./Data/Day06-Data.txt", "r") as reader:
    for line in reader:
        line = line.replace("turn ", "").replace("through ", "")
        directions.append(line[:-1])


def toggle(start, end):

    if light[2] == 0:
        light[2] = 1
    else:
        light[2] = 0


for i in range(1000):
    for j in range(1000):
        lights.append([i, j, 0])

for d in directions:
    d = d.split(" ")
    start = d[1].split(",")
    end = d[2].split(",")
    print(d, start, end)
    # turn lights in range on
    if d[0] == "on":
        pass
    # turn lights in range off
    elif d[0] == "off":
        pass
    # toggle lights in range
    else:
        pass

print(sum([l[2] for l in lights]))
