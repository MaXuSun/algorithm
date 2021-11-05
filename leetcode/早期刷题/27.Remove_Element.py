"""
解题思路：和26一样，使用两个index， 前一个指针index1一直遍历，当nums[index1] != val时，更新nums[index1]=nums[index2]和index1
"""

def removeElement(nums,val):
    """
    time: beats 77.34%
    memory: beats 76.48%
    """
    index1 = index2 = 0
    while index2 < len(nums):
        if nums[index2] != val:
            nums[index1] = nums[index2]
            index1 += 1
        index2 += 1 

    return index1