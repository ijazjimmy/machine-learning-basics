""" First attempt of an implementation of a breath first search in a binary tree.
Similar flaws to the depth-first search algorithim I recently made as it can only
traverse or search for values in binary trees
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if self.data is None:
            self.data = Node(data)
        if self.data > data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        if self.data < data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def __repr__(self):
        return f"Node: {self.data}"

def node_pre_order(node,ar=None):
    if ar is None:
        ar = []
    if node is None:
        return
    ar.append(node.data)
    node_pre_order(node.left,ar)
    node_pre_order(node.right,ar)
    return ar


def bf_traversal(node, path=None):
    if path is None:
        path = []

    if node is None:
        return path

    queue = [node]

    while queue:
        current_node = queue.pop(0)
        path.append(current_node.data)

        if current_node.left is not None:
            queue.append(current_node.left)

        if current_node.right is not None:
            queue.append(current_node.right)

    return path

def bfs(node, target,path=None):
    if path is None:
        path = []

    if node is None:
        return path

    queue = [node]

    while queue:
        current_node = queue.pop(0)
        path.append(current_node.data)
        if current_node.data == target:
            return f"Path to {target}: {path}"

        if current_node.left is not None:
            queue.append(current_node.left)

        if current_node.right is not None:
            queue.append(current_node.right)

    return f"{target} not found in tree:{path}"






node = Node(1)
node.insert(3)
node.insert(4)
node.insert(2)
node.insert(-1)
node.insert(-3)
print(bfs(node,100))