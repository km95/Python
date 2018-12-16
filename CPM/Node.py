class Node(object):
    t0 = 0
    L = 0

    def __init__(self, id, cost):
        self.id = id
        self.CostNode = cost
        if id == 1:
            self.t1 = 1
        else:
            self.t1 = 0

    def wyswietl(self):
        return "Wezel nr %d, moment najwczesniejszy %d, momentnajpozniejszy %d, zapas %d\n" % (
        self.id, self.t0, self.t1, self.L)

    def wyswietl_cost(self):
        print("Wezel nr %d, moment najwczesniejszy %d, momentnajpozniejszy %d, zapas %d," % (
        self.id, self.t0, self.t1, self.L))
        for i in range(len(self.CostNode)):
            print(self.CostNode[i].wyswietl())
