class MyGenerator:
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self
    
    def __next__(self):
        if MyGenerator.current < self.last:
            num = MyGenerator.current
            MyGenerator.current += 1
            return num
        else:
            raise StopIteration
        
gen = MyGenerator(0, 10)
for i in gen:
    print(i)