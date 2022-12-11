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
def count_invisible(r:list[int],c:list[int])->int:
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

# read file, subtract invisible trees from the total count to return the visible trees
def solve_a(filename:str="data"):   
    text = read_file(filename, "\n")
    rows , columns = get_rows_columns(text)
    total = (len(rows)*len(columns))
    invisible = count_invisible(rows,columns)
    visible = total - invisible
    print(visible)
    return visible

solve_a()