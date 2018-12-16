class CostNodes(object):
    def __init__(self, cost, start, stop):
        self.cost = cost
        self.start = start
        self.stop = stop

    def wyswietl(self):
        return "wezel %d -> %d koszt = %d\n" % (self.start, self.stop, self.cost)
