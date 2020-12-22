test = """2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""

# becomes 26.
# becomes 437.
# becomes 12240.
# becomes 13632.

test = test.split("\n")
for t in test:
    prob = t.split()
    print(prob)


operations = "*+"
nums = "0123456789"
