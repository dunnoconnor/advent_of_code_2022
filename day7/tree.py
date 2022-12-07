from node import Node

class Tree:
    # Tree class stores a current node, a list of folders, and a list of folder sizes
    def __init__(self, text:str):
        self.current_node = None
        self.folders = self.build_folders(text)
        self.folder_sizes = self.get_folder_sizes()

    # Create tree structure of folders
    def build_folders(self, lines:list[str]):
        folders = []
        for line in lines:
            if line[0:4] == "$ cd":
                # if changing directory up a level, update the current node
                if line[5:7] == "..":
                    self.current_node = self.current_node.parent
                # if changing directory to a new folder, create a node and update the current node
                else:
                    n = Node(line[5], self.current_node)
                    folders.append(n)
                    self.current_node = n
            # if line begins with a digit, it is a file and its size is added to the current node
            elif line[0].isdigit():
                size = int(''.join(filter(str.isdigit, line)))
                self.current_node.add_size(size)
        # return list of all folders [Node]
        return folders
    
    # return list of all folder sizes [int]
    def get_folder_sizes(self):
        sizes = []
        for f in self.folders:
            sizes.append(f.data)
        sizes.sort()
        return sizes
    
    # return sum (int) of all foler sizes smaller than a given value
    def sum_below_value(self,value:int):
        sum = 0
        for s in self.folder_sizes:
            if s<=value:
                sum  += s
        return sum
    
    # return size (int) of the smallest folder at least as large as the disk space to be cleared
    def clear_space(self, disk:int, req:int):
        free = disk - self.folder_sizes[-1]
        min_size = req - free
    
        for size in self.folder_sizes:
            if size>= min_size:
                return size
