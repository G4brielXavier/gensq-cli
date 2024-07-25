from random import randint

class seq:
    def __init__(self):
        self.seq = []
        
    def __insert__(self, data):
        self.seq.append(data)
        
    def __show__(self):
        for i in self.seq:
            print(i, end=' ')
            
    def __clear__(self):
        self.seq.clear()