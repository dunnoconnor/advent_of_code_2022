from tree import Tree
from read_file import read_file

# read file, create tree, find sum of files smaller than given limit
def solve_a(filename:str="data") -> int:   
    text = read_file(filename, "\n")
    t = Tree(text)
    a = t.sum_below_value(100000)
    print("a: ",a)
    return a

solve_a()