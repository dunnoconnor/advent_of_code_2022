from pos import Pos

class Rope:
    # Node class stores name, x pos, y pos
    def __init__(self,size:int):
        self.nodes = self.gen_nodes(size)
        self.visited = []

    def gen_nodes(self,size) -> list[Pos]:
        nodes = []
        for i in range(size):
            nodes.append(Pos(0,0))
        return nodes

    def move_head(self,line:str):
        dir = line[0]
        val = int(line[1:])
        for i in range(val):
            match dir:
                case "U":
                    self.nodes[0].y += 1
                    self.chase(1)
                case "D":
                    self.nodes[0].y -= 1
                    self.chase(1)
                case "L":
                    self.nodes[0].x -= 1
                    self.chase(1)
                case "R":
                    self.nodes[0].x += 1
                    self.chase(1)
            self.visited.append(str(self.nodes[-1].x)+"*"+str(self.nodes[-1].y))

    def chase(self, n:int):
        if (self.nodes[n].y < self.nodes[n-1].y-1):
                self.nodes[n].y +=1
                if(self.nodes[n].x < self.nodes[n-1].x):
                    self.nodes[n].x +=1
                elif(self.nodes[n].x > self.nodes[n-1].x):
                    self.nodes[n].x -=1
        if (self.nodes[n].y > self.nodes[n-1].y+1):
                self.nodes[n].y -=1
                if(self.nodes[n].x < self.nodes[n-1].x):
                    self.nodes[n].x +=1
                elif(self.nodes[n].x > self.nodes[n-1].x):
                    self.nodes[n].x -= 1
        if self.nodes[n].x > self.nodes[n-1].x+1:
                self.nodes[n].x -=1
                if(self.nodes[n].y < self.nodes[n-1].y):
                    self.nodes[n].y +=1
                elif(self.nodes[n].y > self.nodes[n-1].y):
                    self.nodes[n].y -=1
        if self.nodes[n].x < self.nodes[n-1].x-1:
                self.nodes[n].x +=1
                if(self.nodes[n].y < self.nodes[n-1].y):
                    self.nodes[n].y +=1
                elif(self.nodes[n].y > self.nodes[n-1].y):
                    self.nodes[n].y -=1
        if (n+1)<len(self.nodes):
            self.chase(n+1)
    
    def get_visited(self) -> int:
        print(self.visited)
        print(set(self.visited))
        return len(set(self.visited))