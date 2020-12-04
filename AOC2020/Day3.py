t = []

# test number of trees should be 7
# O, X, O, X, X, O, X, X, X, X
# test = """..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#"""

# t = test.split("\n")

with open("data/Day3.txt", "r") as f:
    for line in f:
        t.append(line[:-1])

# Part 1
# x, y = 0, 0  # x = position in each row, y = row
# tree = 0
# for i in range(len(t) - 1):
#     x += 3
#     y = i + 1
#     x = x % len(t[1])
#     if t[y][x] == "#":
#         tree += 1
#
# print(tree)

# Part 2
def traverse(a, b, t):
    x, y = 0, 0  # x = position in each row, y = row
    tree = 0
    for i in range(len(t) - 1):
        x += a
        y += b
        if y > len(t):
            pass
        else:
            x = x % len(t[1])
            if t[y][x] == "#":
                tree += 1
    return tree


print(
    traverse(1, 1, t)
    * traverse(3, 1, t)
    * traverse(5, 1, t)
    * traverse(7, 1, t)
    * traverse(1, 2, t)
)

