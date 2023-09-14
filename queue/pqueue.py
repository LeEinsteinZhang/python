class PQueue:
    def __init__(self) -> None:
        self.qu = []
        self.size = 0
        self.pri = {0:None, 1:None, 2:None, 3:None, 4:None}

    def __repr__(self) -> str:
        return str(self.qu)

    def enqueue(self, value, pri=0):
        if self.size == 0:
            self.qu.append([value, pri])
            self.pri[pri] = 0
            self.size += 1
        else:
            pass
    def dequeue(self):
        if self.size == 0:
            print("Queue is Empty")
            return
        else:
            return_val = self.qu[0]
            for i in range(self.size - 1):
                self.qu[i] = self.qu[i + 1]
            self.size -= 1
            print(f"Dequeue out {return_val}")
            return return_val
