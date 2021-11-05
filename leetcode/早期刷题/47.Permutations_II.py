"""
解题思路:同样使用递归，但是在使用的时候要去掉重复的数值
这里使用一个技巧，在处理的时候先排序一下
"""

def permuteUnique(nums):
    """
    time: beats 33.43%
    memory: beats 89.99%
    """
    nums.sort()
    def permute(nums):
        if len(nums) == 1:
            return [nums]
        
        result = []
        for i,num in enumerate(nums):
            if i == 0 or nums[i] != nums[i-1]:
                temp = permute(nums[:i]+nums[i+1:])
                for item in temp:
                    result.append([num]+item)
        return result
    return permute(nums)

print(permuteUnique([3,3,0,3]))
        