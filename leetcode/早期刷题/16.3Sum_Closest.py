"""
解题思路：使用two points方法
"""
def threeSumClosest(nums,target):
    nums = sorted(nums)
    dis = abs(sum(nums[0:3])-target)
    result = sum(nums[0:3])
    for i,first in enumerate(nums):
        target2 = target-first
        left = i+1
        right = len(nums)-1
        while left < right:
            if nums[left] + nums[right] == target2:
                return target
            else:

                temp_dis = abs(first+nums[left]+nums[right]-target)
                if temp_dis < dis:
                    result = first + nums[left]+nums[right]
                    dis = temp_dis

                if nums[left] + nums[right] > target2:
                    right -= 1
                else:
                    left += 1
    
    return result
print(threeSumClosest([0,2,1,-3],1))

