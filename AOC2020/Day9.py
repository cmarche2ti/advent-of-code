test = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

puzzle = test.split("\n")


with open("data/Day9.txt") as f:
    puzzle = [line[:-1] for line in f]

preamble = 25


def sums(a, p):
    sum_list = []
    for i in puzzle[a : a + p - 1]:
        for j in puzzle[a + 1 : a + p]:
            if i != j:
                sum_list.append(int(i) + int(j))
    return sum_list


results = []
for i in range(preamble, len(puzzle)):
    if int(puzzle[i]) not in sums(i - preamble, preamble):
        results.append(puzzle[i])

print(results[0])  # 1398413738

puzzle = [int(p) for p in puzzle]
target = int(results[0])
solution = []

for i in range(2, len(puzzle)):
    for j in range(i, len(puzzle)):
        temp = puzzle[j - i : j]
        s = sum(temp)
        if s == target:
            solution = temp
print(solution)
print(sum(solution))
print(max(solution) + min(solution))

