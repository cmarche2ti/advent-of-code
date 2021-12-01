# Part 1
test_data = """199
200
208
210
200
207
240
269
260
263"""
data = []
with open("data/Day01.txt", "r") as f:
    for x in f:
        data.append(x.strip())


print(test_data.split("\n"))
print(data[0:10])


def count_increase(l):
    c = 0
    for index, val in enumerate(l):
        if index > 0:
            if int(val) > int(l[index - 1]):
                c += 1
                print(val, l[index - 1], "increased")
            else:
                print(val, l[index - 1], "decreased")
    print(c)


count_increase(test_data.split("\n"))
count_increase(data)


# part 2


def count_window_increase(l):
    c = 0
    sum_list = [
        (int(val) + int(l[index - 1]) + int(l[index - 2]))
        for index, val in enumerate(l)
        if index > 1
    ]
    count_increase(sum_list)
    # print(sum_list)


# count_window_increase(test_data)
count_window_increase(data)
