"""
解决思路：和Two_Sum, 3Sum, 3Sum Closest一样，使用two points的方法，
但是这里因为是4个相加，和3个还有2个不同，这里使用递归的写法
"""
def fourSum(nums,target):
    def kSum(nums, target, k):
        res = []
        if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
            return res
        if k == 2:
            return twoSum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:        # 避免重复的数据，这也是我之前的3Sum和3Sum Cleftsest 耗时那么长的原因

                for subset in kSum(nums[i + 1:], target - nums[i], k - 1): # 使用递归的方法解决问题
                    res.append([nums[i]] + subset)

        return res

    def twoSum(nums,target):
        res = []
        left, right = 0, len(nums) - 1

        while (left < right):
            curr_sum = nums[left] + nums[right]
            if curr_sum < target or (left > 0 and nums[left] == nums[left - 1]):
                left += 1
            elif curr_sum > target or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
                right -= 1
            else:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
                                                        
        return res

    nums.sort()
    return kSum(nums, target, 4)