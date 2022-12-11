from read_file import read_file

#  create list of row ints and list of column ints
def get_rows_columns(text:str) -> tuple[int,int]:
    r = text
    c = []
    for i in range(len(r[0])):
        for j in range(len(r)):
            if(type(r[j]) == str):
                r[j] = list(r[j])
                c.append([])
            r[j][i] = int(r[j][i])
            c[i].append(r[j][i])
    return (r , c)

#  count all trees not visible from the forest edge
def count_invisible(r:list[int],c:list[int]) -> int:
    count = 0
    for i in range(1,len(r)-1):
        for j in range(1,len(c)-1):
            this_t = r[i][j]
            left = max(r[i][0:j])
            right = max(r[i][j+1:len(r)])
            up = max(c[j][0:i])
            down = max(c[j][i+1:len(c)])
            if this_t <= min([up,down,left,right]):
                count += 1
    return count

# return the product of the views in cardinal directions for a given tree
def multiply_views(tree:int, dirs:list[list[int]]) -> int:
    product = 1
    for d in dirs:
        count = 0
        for t in d:
            count +=1
            if t>=tree:
                break
        product = product*count
    return product

# return the most scenic trees total scenic value
def most_scenic(r:list[int],c:list[int]) -> int:
    ms = 0
    for i in range(1,len(r)-1):
        for j in range(1,len(c)-1):
            tree = r[i][j]
            left = list(r[i][0:j])
            right = list(r[i][j+1:len(r)])
            up = list(c[j][0:i])
            down = list(c[j][i+1:len(c)])
            left.reverse()
            up.reverse()
            view = multiply_views(tree, [left,right,up,down])
            ms = max([ms,view])
    return ms

# read file, create tree, return the most scenic view
def solve_b(filename:str="data") -> int:   
    text = read_file(filename, "\n")
    rows , columns = get_rows_columns(text)
    scenic = most_scenic(rows,columns)
    print(scenic)
    return scenic

solve_b()