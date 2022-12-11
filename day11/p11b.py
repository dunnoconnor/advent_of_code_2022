from read_file import read_file
from monkey import Monkey

def solve_b(filename:str="data") -> int:
    text = read_file(filename, "\n\n")
    Monkey.gen_monkeys(text)
    Monkey.run_turns(10000)
    Monkey.report()
solve_b()