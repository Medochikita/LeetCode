'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
'''

def pivotIndex(nums: list) -> int:
    total = sum(nums)
    left_total = 0

    for i in range(len(nums)):
        right_total = total - left_total - nums[i]

        if right_total == left_total:
            return i
            
        left_total += nums[i]
        
    return -1

print(pivotIndex([2,1,-1]))
