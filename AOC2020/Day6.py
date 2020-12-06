test = """abc

a
b
c

ab
ac

a
a
a
a

b"""

from collections import Counter


f = open("data/Day6.txt")
data = f.readlines()
f.close()


test = "".join(data).split("\n\n")

# test-data ingestion
# test = test.split("\n\n")

total = 0

# part 1
# for t in test:
#     total += len(set(t.replace("\n", "")))
# print(total)

# part 2
for t in test:
    temp_total = 0
    group = t.split("\n")
    size = len(group)
    num = Counter(t.replace("\n", ""))
    for key, val in num.items():
        if val == size:
            temp_total += 1
    total += temp_total

print(total)

