"""
解题思路：使用二分查找，但是二分查找最重要的是确定左半段还是右半段
这里我们先找到确定有序(左右段必然有一段有序)的那一段，然后根据mid和头来判断是否选择这一段
具体看这里(https://www.cnblogs.com/grandyang/p/4325648.html)

二分查找是可能出现 nums[left] == nums[mid]的情况
"""

def search(nums,target):
    """
    time: beats 42.57%
    memory: beats 80.85%
    """
    left,right = 0,len(nums)-1
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] == target: return mid
        if nums[mid] < nums[right]:
            if target > nums[mid] and target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target < nums[mid] and target > nums[left]:
                right = mid - 1
            else:
                left = mid + 1
    return -1

print(search([4,5,6,7,0,1,2],3))
            