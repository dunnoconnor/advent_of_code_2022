from read_file import read_file

# read file, create tree, find sum of files smaller than given limit
def solve_a(filename:str="data") -> int:
    text = read_file(filename, "\n")
    a = text
    print(a)
    return a

solve_a()