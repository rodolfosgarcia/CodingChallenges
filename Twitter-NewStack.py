"""
Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max() which returns the maximum element in the stack 
(return None if the stack is empty). Each method should run in constant time.
"""

class MaxStack:
    def __init__(self):
        self.s = []
        self.max_s = 0

    def push(self, val):
        self.s.append(val)
        self.max_s = max(self.max_s, val)

    def pop(self):
        if s.max():
            self.s.pop()
            self.max_s = max(self.s)

    def max(self):
        return self.max_s if self.max_s else None

s = MaxStack()
print (s.max())
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print (s.max())
# 3
s.pop()
s.pop()
print (s.max())
# 2