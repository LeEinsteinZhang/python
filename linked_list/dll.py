class Node:
    def __init__(self) -> None:
        self.val = None
        self.prev = None
        self.next = None
    
class Dll:
    def __init__(self) -> None:
        self.front = None
        self.back = None
    
    def is_empty(self):
        return self.front == None
    
    def add(self, value):
        new_node = Node()
        new_node.val = value
        if self.front is None:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            new_node.prev = self.back
            self.back = new_node
    
    def remove(self, value):
        current = self.front
        count = 0
        while current is not None:
            if current.val == value:
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.back = current.prev
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.front = current.next  
                count += 1
            current = current.next
        if count == 0:
            print(f"{value} Not exist")

    def __repr__(self) -> str:
        res = []
        current = self.front
        while current is not None:
            res.append(current.val)
            current = current.next
        return str(res)

