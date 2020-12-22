puzzle = [0, 8, 15, 2, 12, 1, 4]
puzz_dict = {}

for index, val in enumerate(puzzle):
    puzz_dict[val] = index + 1

# print(puzz_dict)

endpoint = 30000000
next_value = 0
offset = 1

for i in range(len(puzz_dict) + 1, endpoint):
    if next_value in puzz_dict.keys():
        offset = i - puzz_dict[next_value]
        puzz_dict[next_value] = i
        next_value = offset
    else:
        puzz_dict[next_value] = i
        next_value = 0

# print(puzz_dict)
print(next_value)
