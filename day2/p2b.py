# open file, read data, split by newline
f = open("p2data.txt", "r")
text = f.read()
f.close()
rounds = text.split("\n")

# accumulator for total points
points = 0

# dict for point values from lose/draw/win
resolution_bonus = {"X":0,"Y":3,"Z":6}

#dict for results
results = {"A Y": 1, "A Z": 2, "A X": 3, "B Y": 2, "B Z": 3, "B X":1, "C Y":3, "C Z": 1, "C X": 2}

# each round, add points for result plus shape bonus
for r in rounds:
    points += results[r] + resolution_bonus[r[-1]]

# total score
print(points)