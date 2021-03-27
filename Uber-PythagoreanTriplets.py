"""
Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

Example:
Input: [3, 5, 12, 5, 13]
Output: True
Here, 5^2 + 12^2 = 13^2.
"""

def findPythagoreanTriplets(nums):
    squared = []
    for value in nums:
        squared.append(value**2)
    squared.sort()
    #print (squared)

    #from last index to third index
    for c in range(len(nums)-1, 1, -1):
        a = 0
        b = c - 1
        #print('a '+ str(a) + ' b ' + str(b) + ' c ' + str(c))
        while (a < b):
            #print(str(squared[a]) + '  ' + str(squared[b]) + '  ' + str(squared[c]))
            if squared[c] == squared[a] + squared[b]:
                return True
            
            #rules for moving pointers A, B
            elif squared[c] > (squared[a] + squared[b]):
                a += 1
            elif squared[c] < (squared[a] + squared[b]):
                b -= 1
    return False

print (findPythagoreanTriplets([3, 12, 5, 13]))
# True

