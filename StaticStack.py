
class staticStack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.data = []

    def push(self, value):
        if not(self.isFull()):
            self.top+=1
            self.data.append(value)
        else:
            print("The stack is full.")

    def pop(self):
        if not(self.isEmpty()):
            removed = self.data.pop(self.top)
            self.top-=1
            return removed
        else:
            print("The stack is empty.")

    def isEmpty(self):
        return self.top==-1

    def isFull(self):
        return self.top+1==self.size



    def Top(self):
        if self.isEmpty():
            return
        else:
            return self.data[self.top]




if __name__ == '__main__':
    s = staticStack(10)
    s.push(1)
    print(s.Top())
    s.push(12)
    print(s.Top())
    s.pop()
    print(s.Top())
    s.push(13)
    s.push(14)
    s.push(15)
    s.push(15)
    s.push(15)
    s.push(15)
    s.push(15)
    s.push(15)
    s.push(15)
    s.push(15)

