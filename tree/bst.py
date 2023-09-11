class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def node_insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.node_insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.node_insert(node.right, value)

    def node_find(self, node, value):
        if node is None:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            return self.node_find(node.left, value)
        else:
            return self.node_find(node.right, value)

    def node_inorder_traversal(self, node, res):
        if node is not None:
            self.node_inorder_traversal(node.left, res)
            res.append(node.value)
            self.node_inorder_traversal(node.right, res)


class BST:
    def __init__(self):
        self.root = None
        self.len = 0

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            self.len += 1
        else:
            self.root.node_insert(self.root, value)
            self.len += 1

    def find(self, value):
        return self.root.node_find(self.root, value)

    def inorder_traversal(self):
        res = []
        self.root.node_inorder_traversal(self.root, res)
        return res
