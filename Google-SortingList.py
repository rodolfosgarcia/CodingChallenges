"""
Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]
"""


def sortNums(nums):
    q1 = 0
    q2 = 0
    q3 = 0
    for n in nums:
        if n == 1:
            q1 += 1
        elif n == 2:
            q2 += 1
        elif n == 3:
            q3 += 1
    return [1]*q1 + [2]*q2 + [3]*q3

print (sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]