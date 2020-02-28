"""
Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k.
If either does not exist, then print them as None.
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    """
            8
        4       12
    2     6  10    14     
    """
    if root_node == None:
        return floor, ceil
    
    if root_node.value == k:
        return k, k

    if root_node.value > k:
        return findCeilingFloor(root_node.left, k, floor, root_node.value)
    if root_node.value < k:
        return findCeilingFloor(root_node.right, k, root_node.value, ceil)
    
root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 


for i in range(1, 14):
    print (str(i) + '  ' + str(findCeilingFloor(root, i)))

print(findCeilingFloor(root, 5))
# (4, 6)