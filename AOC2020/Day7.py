test = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
# How many bags can contain a shiny gold bag?  Answer: 4


def contains(n):
    if "no other" in rd[n]:
        return False

    if "shiny gold" in rd[n]:
        return True

    bags = rd[n].split(", ")
    colors = []
    for x in bags:
        y = x.split(" ")
        colors.append(y[1] + " " + y[2])

    for x in colors:
        if contains(x):
            return True

    return False


def countbags(n):
    if "no other" in rd[n]:
        return 0

    bags = rd[n].split(", ")
    t = 0
    for x in bags:
        y = x.split(" ")
        t += int(y[0]) + (int(y[0]) * countbags(y[1] + " " + y[2]))

    return t


with open("data/Day7.txt", "r") as f:
    r = f.read().split("\n")

rd = {i.split(" contain ")[0][:-5]: i.split(" contain ")[1] for i in r}

t = 0
for x in rd.keys():
    if contains(x):
        t += 1

print(t)
print(countbags("shiny gold"))

