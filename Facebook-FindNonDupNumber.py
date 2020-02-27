"""
Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1
"""

def singleNumber(nums):
    d = {}
    for i, n in enumerate(nums):
        if d.get(n) == None:
            d[n] = i
        else:
            d.pop(n)
    for key in d:
        return key

print (singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
