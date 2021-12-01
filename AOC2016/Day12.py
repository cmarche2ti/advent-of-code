puzzle = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 19 c
cpy 11 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""

# puzzle = """cpy 41 a
# inc a
# inc a
# dec a
# jnz a 2
# dec a"""
data = puzzle.split("\n")
print(data)
register = {"a": 0, "b": 0, "c": 1, "d": 0}


def cpy(c):
    x, y = c.split()[1], c.split()[2]
    if x in "abcd":
        register[y] = register.get(x)
    else:
        register[y] = int(x)


def inc(c):
    a = c.split()[1]
    print(a)
    register[a] += 1


def dec(c):
    a = c.split()[1]
    register[a] -= 1


def jnz(c):
    a, b = c.split()[1], c.split()[2]
    print(a, b)
    # if a == "0" or .get(a) == 0:
    #     return 1
    # else:
    #     return int(b)
    try:
        zero_val = register[a]  # Check if the given val is a register.
    except KeyError:
        zero_val = int(a)  # Otherwise, it's just an integer.
    if zero_val == 0:
        return 1
    return int(b)


i = 0

while i < len(data):
    print(data[i])

    if "cpy" in data[i]:
        cpy(data[i])
        i += 1
    elif "inc" in data[i]:
        inc(data[i])
        i += 1
    elif "dec" in data[i]:
        dec(data[i])
        i += 1
    else:
        i += jnz(data[i])
    print(register)
    print(f"i = {i}")

print(register["a"])

