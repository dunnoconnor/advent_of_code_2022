# open file, read data, split by newline
f = open("data.txt", "r")
text = f.read()
f.close()
pairs = text.split("\n")

count=0

for p in pairs:
    camps = p.split(",")
    camps = [camps[0].split("-"),camps[1].split("-")]

    campA = [int(camps[0][0]),int(camps[0][1])]
    campB = [int(camps[1][0]),int(camps[1][1])]
    
    if(campA[0]<=campB[1] and campA[1]>=campB[0]):
        count +=1
        
print(count)