import pandas as pd
import math

# data_list = data.split("\n")
# data_clean = [num.strip() for num in data_list]
# # print(data_clean)

# # fuel = [math.floor(int(num)/3) - 2 for num in data_clean]
# # print(sum(fuel))
# fuel = []
# for num in data_clean:
#     fuel_module = 0
#     temp_fuel = math.floor(int(num)/3) - 2
#     while temp_fuel > 0:
#         fuel_module = fuel_module + temp_fuel 
#         temp_fuel = math.floor(temp_fuel/3) - 2
#     fuel.append(fuel_module)

# print(sum(fuel))
        
## Joel Grus Solution
def fuel(mass: int) -> int:
    return mass//3-2

assert fuel(12) == 2
assert fuel(14) == 2
assert fuel(1969) == 654
assert fuel(100756) == 33583

with open('input.txt') as f:
    masses = [int(line.strip()) for line in f]
    part1 = sum(fuel(mass) for mass in masses)

print(part1)

def fuel_for_fuel(mass:int) -> int:
    total = 0
    next_fuel = fuel(mass)
    while next_fuel > 0:
        total += next_fuel
        next_fuel = fuel(next_fuel)
    return total

assert fuel_for_fuel(14) == 2
assert fuel_for_fuel(1969) == 966
assert fuel_for_fuel(100756) == 50346

part2 = sum(fuel_for_fuel(mass) for mass in masses)
print(part2)