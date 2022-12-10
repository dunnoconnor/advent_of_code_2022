from read_file import read_file
from rope import Rope

# read file, create tree, find sum of files smaller than given limit
def solve_b(filename:str="data") -> int:
    text = read_file(filename, "\n")
    b = text
    print(b)

solve_b()