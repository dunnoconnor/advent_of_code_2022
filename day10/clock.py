class Clock:
    # Clock class stores name, x pos, y pos
    def __init__(self):
        self.cycles = 1        
        self.x = 1
        self.signals = []
        self.checkpoint = 20

    def run_clock(self,text:str):
        for l in text:
            self.execute(l)

    def execute(self,l:str):
        if l != "noop":
            _ , v = l.split(" ")
            self.check_cycle()
            self.x += int(v)
        self.check_cycle()


    def check_cycle(self):
        if (self.cycles == self.checkpoint) and (self.cycles <= 220):
            self.signals.append(self.cycles*self.x)
            print(f'During the {self.checkpoint}th cycle, register X has the value {self.x}, so the signal strength is {self.checkpoint} * {self.x} = {self.signals[-1]}.')
            self.checkpoint += 40
        self.cycles += 1
