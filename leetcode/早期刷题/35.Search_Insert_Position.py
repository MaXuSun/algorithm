"""
解题思路：使用二分法，下面这个写法才是正宗的二分法写法。二分法通过更改判断条件可以实现一些特定任务
"""
def searchInsert(nums,target):
    """
    time: beats 90.46%
    memory: beats 81.15%
    """
    left,right = 0,len(nums)-1
    while left <= right:
        mid = (left+(right-left)//2)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid+1
        elif target < nums[mid]:
            right = mid - 1
    return left

print(searchInsert([1,3,5],2))
