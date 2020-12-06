# row 70, column 7, seat ID 567.
# row 14, column 7, seat ID 119.
# row 102, column 4, seat ID 820.
seat = """BFFFBBFRRR 
FFFBBBFRRR    
BBFFBBFRLL"""

seat = seat.split("\n")
seat_list = []


with open("data/Day5.txt", "r") as f:
    for line in f:
        seat_list.append(line)


def find_row(s):
    rows = list(range(128))
    row_index = 64
    index = 0
    while index < 7:
        if s[index] == "F":
            rows = rows[:row_index]
        else:
            ind = -1 * row_index
            rows = rows[ind:]
        index += 1
        row_index = row_index // 2
    print(rows)
    return rows[0]


def find_col(s):
    cols = list(range(8))
    col_index = 4
    index = 7
    while index < 10:
        if s[index] == "L":
            cols = cols[:col_index]
        else:
            ind = -1 * col_index
            cols = cols[ind:]
        index += 1
        col_index = col_index // 2
    return cols[0]


# tests
# print("FBFBBFFRLR", find_row("FBFBBFFRLR"), find_col("FBFBBFFRLR"))
# print("FBFBBFBRLR", find_row("FBFBBFBRLR"), find_col("FBFBBFBRLR"))

# part 1
seat_id = [8 * find_row(ticket) + find_col(ticket) for ticket in seat_list]
# print(max(seat_id))

# part 2

seats_ordered = sorted(seat_id)
missing = [
    val for val in range(min(seats_ordered), max(seats_ordered)) if val not in seat_id
]

for val in range(max(seats_ordered)):
    a = val + 1
    b = val - 1
    if val not in seats_ordered:
        if a in seat_id and b in seat_id:
            print(val)

