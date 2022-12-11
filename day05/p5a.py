# open file, read data, split by symbol param
def read_file(name, symbol):
    f = open(f'{name}.txt', "r")
    text = f.read()
    f.close()
    return text.split(symbol)

# clean stacks: remove unneeded chars, split, and reverse 
def get_stacks(s):
    s = s.translate(str.maketrans('', '', '[]'))
    s = s.split('\n')
    s.reverse()
    return s

# clean moves: remove unneeded chars and split
def get_moves(m):
    m = m.translate(str.maketrans('', '', 'movefrmt'))
    return m.split('  ')

#  move (n)umber of (c)rates (f)rom one stack (t)o another 
def move_crate(n, f, t):
    for i in range(n):
        c = stacks[f-1].pop()
        stacks[t-1].append(c)

#  call functions to clean data
stack_txt = read_file('stacks',"\n\n")
move_txt = read_file('moves','\n')
stacks = list(map(get_stacks, stack_txt))
moves = list(map(get_moves, move_txt))

# moves crates
for m in moves:
    move_crate(int(m[0]),int(m[1]),int(m[2]))

#print the top crate in each stack
for s in stacks:
    print(s[-1])