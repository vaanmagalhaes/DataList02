class Nodo:
    def __init__ (self, data=0, next_nodo=None):
        self.data = data
        self.next = next_nodo

    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def __repr__(self):
        return "[" + str(self.first) + "]"

