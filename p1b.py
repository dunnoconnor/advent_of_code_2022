# open file, read data, split by newline
f = open("p1data.txt", "r")
text = f.read()
f.close()
elves = text.split("\n\n")

# accumulator for top 3 calorie counts
most_cals = [0, 0, 0]

for elf in elves:
  # split each elf into list of calories, convert to int, then sum the lists
  cals_list = elf.split("\n")
  this_cals = sum(list(map(int, cals_list)))
  # if current value > third highest, replace it
  most_cals[0] = max(most_cals[0], this_cals)
  #sort top 3
  most_cals.sort()

# part 1 solution
print(f"The elf carrying the most calories has: {most_cals[-1]}")

# part 2 solution
top_three = sum(most_cals)
print(f"The sum of the top three most calories is: {top_three}")
