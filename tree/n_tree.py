class TreeNode:
    def __init__(self, value=None) -> None:
        self.val = value
        self.children = []
    
    def node_add(self, value):
        self.children.append(TreeNode(value))

    def node_traversal(self, node):
        

class NTree:
    def __init__(self) -> None:
        self.root = None

    def is_empty(self):
        return self.root == None
    
