"""
解题思路：使用两个index,一前一后，前面的如果比后面的值大，就更新后面的值，并更新后index。如果一样大，就更新前一个index
"""
def removeDuplicates(nums):
    """
    time: beats 73.80%
    memory: 97.63%
    """
    index1 = 0
    index2 = 1
    while index2<len(nums):
        if nums[index2] > nums[index1]:
            nums[index1+1] = nums[index2]
            index1 += 1
        else:
            index2 += 1
    # print(nums)
    return index1 + 1

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))