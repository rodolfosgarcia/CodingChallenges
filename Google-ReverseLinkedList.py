#!/usr/bin/env python

"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?

Example:
Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
  
    # Function to print the list
    def printList(self):
        node = self
        output = '' 
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)
        
    # Iterative Solution
    def reverseIteratively(self, head):
        # Implement this.
        prev = None
        curr = head
        while curr is not None:
            #saving next for continuing loop
            nxt = curr.next
            #updating/reversing current node
            curr.next = prev
            #preparing for the next node
            prev = curr
            curr = nxt
        head = prev

    # Recursive Solution      
    def reverseRecursively(self, head):
        # Implement this.
        if head == None:
            return head
        if head.next == None:
            return head
        
        #will always return the last element, that should be the first (head) at the end of the reversing
        head1 = self.reverseRecursively(head.next)
        #reverse the link from 1 -> 2 to 1 <- 2
        head.next.next = head
        #empty the next, as the recursive call go back it will link correctly but not the last element that will remain None
        head.next = None
        return head1
        

# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

#print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
#testHead.reverseIteratively(testHead)
testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4