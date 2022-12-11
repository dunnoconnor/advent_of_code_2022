# open file, read data, split by symbol param
def read_file(name, symbol):
    f = open(f'{name}.txt', "r")
    text = f.read()
    f.close()
    return text.split(symbol)