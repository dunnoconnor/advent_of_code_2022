from read_file import read_file
from clock import Clock

# read file, create tree, find sum of files smaller than given limit
def solve_b(filename:str="data") -> int:
    text = read_file(filename, "\n")
    c = Clock(40,6)
    c.run_clock(text)
    c.prnt_crt()

solve_b()