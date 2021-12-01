puzzle = """Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.
Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.
Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.
Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.
Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.
Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds."""

# name 0, speed 3, time 6, rest -2

reindeer_list = []
results = []

for p in puzzle.split("\n"):
    d = {}
    d["name"] = p.split()[0]
    d["speed"] = int(p.split()[3])
    d["time"] = int(p.split()[6])
    d["rest"] = int(p.split()[-2])
    reindeer_list.append(d)


for r in reindeer_list:
    race_time = 2503
    distance = 0
    distances = []
    result = {}
    elapsed_time = 0
    result["name"] = r["name"]
    while race_time > 0:
        race_time -= 1
        elapsed_time += 1
        distance += r["speed"]
        distances.append(distance)
        if elapsed_time % r["time"] == 0:
            race_time -= r["rest"]
    result["dist"] = distance
    result["dist_list"] = distances
    print(result)
    results.append(result)

race_time = 2503
points = []
for i in range(len(results["dist_list"])):
    for r in results:
        rpoints = {"points": 0}
        rpoints["name"] = r["name"]
        rpoints["points"] += 1
    points.append(rpoints)

print(points)
