class Stack:
    """

    """
    def __init__(self) -> None:
        self.stack = []
        self.num = 0
    
    def __repr__(self) -> str:
        return str(self.stack)
    
    def is_empty(self):
        return self.num == 0
    
    def size(self):
        return self.num

    def push(self, value):
        if self.num == 0:
            self.stack.append(value)
            self.num = 1
        else:
            self.stack.append(value)
            self.num += 1
    
    def pop(self):
        if self.num == 0:
            print("Stack is empty")
            return
        else:
            self.num -= 1
            return_val = self.stack[self.num]
            self.stack[self.num] = None
            print(f"Pop out {return_val}")
            return return_val
