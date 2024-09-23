"""First attempt at a depth first search through a binary through algorithim. Very basic as it only works for binary trees and does not support graphs,
there is no method to delete or edit nodes. There is not much error feedback for the case where the target is not in the binary tree. The stack should be able
to backtrack, i.e (Pop elements and go backwards which would make the code more efficent).
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def insert(self,data):
        if self.data is None:
            self.data = data
        elif self.data > data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif self.data < data:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def __repr__(self):
        return f'Node({self.data})'

def pre_order(node, dataset=None):
    if dataset is None:
        dataset = []
    if node is not None:
        dataset.append(node.data)
        pre_order(node.left,dataset)
        pre_order(node.right,dataset)
        return dataset

def find_number(node,target,stack=None):
    if stack is None:
        stack = []
    if node is None:
        return
    stack.append(node.data)
    if node.data == target:
        return stack
    check_left = find_number(node.left,target,stack)
    if check_left:
        return check_left
    check_right = find_number(node.right, target, stack)
    if check_right:
        return check_right



n1 = Node(1)
n1.insert(3)
n1.insert(2)
n1.insert(-4)
n1.insert(-8)
n1.insert(-11)
n1.insert(14)
n1.insert(9)
print(find_number(n1,-11))
