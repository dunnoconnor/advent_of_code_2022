class Clock:
    # Clock class stores name, x pos, y pos
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.cycles = 0      
        self.x = 1
        self.signal = 0
        self.checkpoint = 20
        self.crt = self.gen_crt()

    def gen_crt(self):
        s = []
        for _ in range(self.width*self.height):
            s.append(".")
        return s

    def prnt_crt(self):
        p = 0
        for _ in range(self.height):
            row = "".join(self.crt[p:(p+self.width)])
            print(row)
            p+=self.width

    def draw(self):
        row_x = self.cycles % 40
        if(self.x<=(row_x+1) and self.x>=(row_x-1)):
            self.crt[self.cycles] = "#"
    
    def run_clock(self,text:str):
        for l in text:
            self.execute(l)

    def execute(self,l:str):
        self.check_cycle(0)
        if l != "noop":
            _ , v = l.split(" ")
            self.check_cycle(int(v))

    def check_cycle(self,v:int):
        self.draw()
        self.cycles += 1
        if (self.cycles == self.checkpoint):
            self.signal += (self.cycles*self.x)
            print(f'During the {self.checkpoint}th cycle, register X has the value {self.x}, so the signal strength is {self.checkpoint} * {self.x} = {self.signal}.')
            self.checkpoint += 40
        self.x += v
