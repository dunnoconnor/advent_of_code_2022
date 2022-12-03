# open file, read data, split by newline
f = open("data.txt", "r")
text = f.read()
f.close()
sacks = text.split("\n")

# find the matching chars
def findMatches(list):
    m = ""
    for string in list:
        # split each string and covert to set
        comp1, comp2 = set(string[:len(string)//2]), set(string[len(string)//2:])
        # compare sets for intersection
        match = comp1.intersection(comp2)
        # add matches to accumulator
        m += match.pop()
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