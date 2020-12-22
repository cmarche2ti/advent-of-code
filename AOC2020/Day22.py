player_1 = """43
36
13
11
20
25
37
38
4
18
1
8
27
23
7
22
10
5
50
40
45
26
15
32
33"""

player_2 = """21
29
12
28
46
9
44
6
16
39
19
24
17
14
47
48
42
34
31
3
41
35
2
30
49"""

player_1 = player_1.split("\n")
player_2 = player_2.split("\n")


while len(player_1) > 0 and len(player_2) > 0:
    print(len(player_1), len(player_2))
    card1, card2 = int(player_1.pop(0)), int(player_1.pop(0))
    if card1 > card2:
        player_1.append(card1)
        player_1.append(card2)
    else:
        player_2.append(card2)
        player_2.append(card1)
    print(player_1)


print(player_1)
print(player_2)


def score(player):
    player = player.reverse()
    score = 0
    for i in range(1, len(player)):
        score = score + i * int(player[i - 1])
    return score


print("Player 2 Wins: " + str(score(player_2)))
