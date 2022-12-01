f = open("p1data.txt", "r")
text = f.read()
f.close()
food = text.split("\n")
most_food = 0
this_food = 0

for i in food:
  if i == "":
    if this_food > most_food:
      most_food = this_food
    this_food = 0
  else:
    this_food += int(i)

print(most_food)
