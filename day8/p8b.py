from read_file import read_file

# read file, create tree, find sum of files smaller than given limit
def solve_b(filename:str="data"):   
    text = read_file(filename, "\n")
    b = text
    print("b: ",b)
    return b

solve_b("sample")