# open file, read data, split by newline
f = open("p2data.txt", "r")
text = f.read()
f.close()
rounds = text.split("\n")

# accumulator for total points
points = 0

# dict for point values from your shape
shape_bonus = {"X":1,"Y":2,"Z":3}

#dict for results
results = {"A X": 3, "B Y": 3, "C Z": 3, "A Y": 6, "B Z": 6, "C X": 6, "A Z": 0, "B X":0, "C Y":0}

# each round, add points for result plus shape bonus
for r in rounds:
    points += results[r] + shape_bonus[r[-1]]

# total score
print(points)