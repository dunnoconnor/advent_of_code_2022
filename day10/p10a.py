from read_file import read_file
from clock import Clock

# read file, create tree, find sum of files smaller than given limit
def solve_a(filename:str="data") -> int:
    text = read_file(filename, "\n")
    c = Clock(40,6)
    c.run_clock(text)
    print(c.signal)

solve_a("sample")