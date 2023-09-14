class Queue:
    def __init__(self) -> None:
        self.qu = []
        self.size = 0

    def __repr__(self) -> str:
        return str(self.qu)

    def enqueue(self, value):
        self.qu.append(value)
        self.size += 1

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
