timestamp = 1000053
bus = "19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,523,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,23,x,x,x,x,x,29,x,547,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"
bus = bus.split(",")
depart = {}


def departure_time(timestamp, t):
    time = 0
    i = 0
    while time < timestamp:
        time = int(t) * i
        i += 1
    return time - timestamp


for b in bus:
    if b != "x":
        depart[b] = departure_time(timestamp, b)

print(depart)

test = "1 w 2 r 3g"
print(test.title())
