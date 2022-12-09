from read_file import read_file
from rope import Rope

# read file, create tree, find sum of files smaller than given limit
def solve_a(filename:str="data") -> int:
    text = read_file(filename, "\n")
    rope = Rope(2)
    for l in text:
        rope.move_head(l)
    a = rope.get_visited()
    print(a)

solve_a("sample")