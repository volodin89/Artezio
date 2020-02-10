class EvenIterator(object):

    def __init__(self, lst):
        self.lst = lst
        self.cursor = 1

    def __iter__(self):
        return self

    def __next__(self):
        pos = self.cursor
        if pos < len(self.lst):
            self.cursor += 2
            return self.lst[pos]
        else:
            raise StopIteration



a=EvenIterator([1,2,3,4,5])
print(next(a))
