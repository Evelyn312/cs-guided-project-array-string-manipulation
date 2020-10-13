"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
def pivot_index(nums):
    print(nums)
    for i in range(1,len(nums)):
        # print(i)
        # print(sum(nums[:(i)]))
        # print(sum(nums[(i+1):len(nums)]))
        if sum(nums[:(i)]) == sum(nums[(i+1):len(nums)]):
            result = i
            break
        else:
            result = -1
    print(result)
    return result
    
pivot_index([1,2,3,20,6,26])

