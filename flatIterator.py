
class FlatIterator:

    def __init__(self, list_of_list):
        self.l = list_of_list
        self.a = 0
        self.b = 0
        self.stop = False

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stop:
            while self.a < len(self.l):
                if self.b < len(self.l[self.a]):
                    item = self.l[self.a][self.b]
                    self.b += 1
                    return item
                self.a += 1
                self.b = 0
            self.stop = True
        raise StopIteration