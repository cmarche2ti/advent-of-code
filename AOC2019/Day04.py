from collections import Counter

double = False
greater = True
count = 0


def password(num):
    double = False
    greater = True
    num = str(num)
    p = Counter(num)
    for c in range(0, len(num) - 1):
        if num[c] == num[c + 1] and p[num[c]] == 2:
            double = True
        if num[c] > num[c + 1]:
            greater = False
    if double and greater:
        return True
    else:
        return False


print(password(111111))  # True
print(password(223450))  # False
print(password(123789))  # False

for num in range(347312, 805915):
    if password(num):
        count += 1

print(count)
