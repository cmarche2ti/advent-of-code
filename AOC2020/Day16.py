rules = """departure location: 39-715 or 734-949
departure station: 30-152 or 160-959
departure platform: 34-780 or 798-955
departure track: 32-674 or 699-952
departure date: 38-55 or 74-952
departure time: 45-533 or 547-970
arrival location: 27-168 or 191-969
arrival station: 43-585 or 599-953
arrival platform: 40-831 or 837-961
arrival track: 37-293 or 301-974
class: 40-89 or 112-950
duration: 25-600 or 625-970
price: 45-318 or 341-954
route: 40-898 or 912-968
row: 38-872 or 881-958
seat: 37-821 or 831-958
train: 26-343 or 365-956
type: 37-857 or 872-960
wagon: 36-425 or 445-972
zone: 44-270 or 286-967"""

your_ticket = [
    223,
    139,
    211,
    131,
    113,
    197,
    151,
    193,
    127,
    53,
    89,
    167,
    227,
    79,
    163,
    199,
    191,
    83,
    137,
    149,
]
puzzle = []
with open("data/Day16.txt", "r") as f:
    for line in f:
        puzzle.append(line.replace("\n", "").split(","))


rules = rules.split("\n")
good_ranges = []
seats = []

for rule in rules:
    rg = rule.split(":")[1]
    for r in rg.split(" or "):
        good_ranges.append(r.strip())

for r in good_ranges:
    x, y = r.split("-")
    a, b = int(x), int(y)
    for i in range(a, b + 1):
        if i not in seats:
            seats.append(i)

print(seats)

bad_tix = []
test = False

bad_tickets = []

for p in puzzle:
    for val in p:
        if int(val) in seats:
            print(val, "good")
        else:
            print(val, "bad")
            bad_tickets.append(int(val))
print(sum(bad_tickets))

