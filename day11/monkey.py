class Monkey:

    monkeys = []
    lcm = 1

    def __init__(self, num:int, items:list[int], op:str, val:int, mod:int, t:int, f:int):
        self.num = num
        self.items = items
        self.op = op
        self.val = val
        self.mod = mod
        self.t = t
        self.f = f
        self.count = 0
    
    def gen_monkeys(text:list[str]):
        for t in text:
            lines = t.split('\n')
            num=lines[0][-2]
            items = str(lines[1][18:]).split(",")
            items = list(map(int,items))
            op = lines[2][23]
            val = lines[2][24:]
            if(val==" old"):
                op = "**"
                val = "2"
            mod = int(str(lines[3]).split(" ")[-1])
            t = int(lines[4][-1])
            f = int(lines[5][-1])
            m = Monkey(num,items,op,val,mod,t,f)
            Monkey.lcm = int(Monkey.lcm * mod)
            Monkey.monkeys.append(m)

    def run_turns(t_count:int):
        for _ in range(t_count):
            for m in Monkey.monkeys:
                m.turn()

    def turn(self):
        for _ in range(len(self.items)):
            self.count += 1
            worry = self.items.pop(0)
            worry = eval(str(worry) + self.op + self.val)
            # Part II only
            worry = worry % Monkey.lcm
            # Part I only
            # worry = worry // 3
            if(worry%self.mod==0):
                Monkey.monkeys[self.t].items.append(worry)
            else:
                Monkey.monkeys[self.f].items.append(worry)

    def report():
        counts = []
        for m in Monkey.monkeys:
            print(f"Monkey {m.num} inspected items {m.count} times")
            counts.append(m.count)
        counts.sort()
        business = counts[-1]*counts[-2]
        print(f"Monkey Business: {business}")
        