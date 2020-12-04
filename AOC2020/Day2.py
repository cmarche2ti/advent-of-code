from collections import Counter

# Part 1
f = open("data/Day2.txt", "r")
count = 0
for x in f:
    password = x.split()
    num = password[0].split("-")
    num_min = int(num[0])
    num_max = int(num[1])
    letter = password[1][0]
    test = Counter(password[2])
    if test[letter] >= num_min and test[letter] <= num_max:
        count += 1
f.close()
print(count)

f = open("data/Day2.txt", "r")
# f = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

# Part 2
def part2(text_file):
    count2 = 0
    for x in f:
        password = x.split()
        num = password[0].split("-")
        num_min = int(num[0])
        num_max = int(num[1])
        letter = password[1][0]
        word = password[2]
        if (word[num_min - 1] == letter and word[num_max - 1] != letter) or (
            word[num_min - 1] != letter and word[num_max - 1] == letter
        ):
            count2 += 1
    f.close()
    return count2


print(part2(f))
