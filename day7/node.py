class Node:
    # Node class stores a folder name, data size, and parent directory
    def __init__(self, name:str, parent:object):
        self.name = name
        self.data = 0
        self.parent = parent
    
    # add the current file size to this folder and recursively to parent folder(s)
    def add_size(self, size:int):
        if(self.parent):
            self.parent.add_size(size)
        self.data += size