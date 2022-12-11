# open file, read data, split by newline
f = open("data.txt", "r")
text = f.read()
f.close()
sacks = text.split("\n")

# find the matching chars
def findMatches(list):
    count = 0
    m = ""
    while count<len(list):
        # convert three sequential strings to sets
        elf1, elf2, elf3 = set(list[count]), set(list[count+1]), set(list[count+2])
        # compare sets for intersection
        match = elf1.intersection(elf2,elf3)
        # add matches to accumulator
        m += match.pop()
        # increment counter by three
        count += 3
    # return string of all matches
    return m

# sum values of chars in string
def sumString(string):
    sum = 0
    # for uppercase/lowercase, offset from unicode value
    for c in string:
        if c.isupper():
            sum += (ord(c) - 38)
        else:
            sum += (ord(c) - 96)
    return sum

# invoke functions, print sum of values
matches = findMatches(sacks)
sum = sumString(matches)
print(sum)