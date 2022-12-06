# open file, read data, split by newline
f = open("data.txt", "r")
text = f.read()
f.close()

# loop through text creating slices of the marker length
def find_marker(text, num):
    for i in range(0,(len(text)-num)):
        # *sub creates a list - trimming repeated elements
        sub = [*set(text[i:(i+num)])]
        # if no repeats are trimmed, return the end of this slice
        if(len(sub)==num):
            return (i+num)

# call function, specifying slice length
print(find_marker(text, 4))