#!/usr/bin/env python

"""
Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
"""

class Solution:
    def isValid(self, s):
        invalid = []
        
        if (')' or ']' or '}') in s[:0]:
            return False
        
        if ('(' or '[' or '{') in s[-1:]:
            return False

        transl = {'(':')', '[':']', '{':'}'}
        
        for char in s:
            #if char == '(' or char == '[' or char == '{':
            if char in '([{':
                invalid.append(char)
            #if char == ')' or char == ']' or char == '}':
            if char in ')]}':
                if transl[invalid[-1]] == char:
                    invalid.pop()
        if not invalid:
            return True
        else:
            return False


# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))