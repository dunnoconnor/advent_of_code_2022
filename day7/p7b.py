from tree import Tree
from read_file import read_file

# read file, create tree, find smallest file that will clear enough space
def solve(filename:str="data"):   
    text = read_file(filename, "\n")
    t = Tree(text)
    a = t.sum_below_value(100000)
    b = t.clear_space(70000000,30000000)
    print("a: ", a)
    print("b: ", b)
    return b

solve()