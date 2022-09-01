class Stack:
    def __init__(self):
        self.lst = []

    def push(self, value):
        self.lst.append(value)

    def pop(self):
        return self.lst.pop()

    def display(self):
        return self.lst
    
    def insert(self, index, value):
        self.lst.insert(index, value)
    
    def remove(self, index):
        self.lst.pop(index)

s1 = Stack()

s1.push(1)
s1.pop()
s1.push(2)
s1.push(100)
s1.insert(1, 9)
s1.remove(0)

s2 = Stack()
s2.push(1111)
s2.push(23)

s3 = Stack()
s3.push(10000)
s3.push(123)
s3.push(1)
s3.push(111)
s3.push(13)
s3.insert(2, 999)
s3.remove(0)

print(s3.display())
