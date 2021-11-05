"""
解决方法：
v1: 一个简单的想法，将3Sum转成2Sum的问题。使用这种方法时，由于元素有重复的，所以先排序。但是这种方法耗时比较长，占用空间比较大。
v2: 使用two points 方法
"""

def threeSum(nums):
    """
    time: beats 5.00% 
    memory: beats 18.08%
    """
    if len(nums) < 3:
        return []
    result = []
    nums = sorted(nums) # 排序
    for i,num1 in enumerate(nums):
        maps = {}
        for j,num2 in enumerate(nums[i+1:],i+1):
            maps.setdefault(num2,j)
            k = maps.get(-num1-num2)

            if k is not None and k != j and k!=i and i!=j:
                temp = [num1,num2,-num1-num2]
                if temp not in result:
                    result.append(temp)
                
    return result

def threeSum(nums):
    """
    time: beats 9.60%
    memory: beats 51.25
    """
    if len(nums) < 3:
        return []
    result = []
    nums = sorted(nums)

    for i,num1 in enumerate(nums):
        left = i+1
        right = len(nums)-1
        while left < right:
            if nums[left] + nums[right] < -num1 :
                left += 1
            elif nums[left] + nums[right] > -num1:
                right -= 1
            else:
                temp = [num1,nums[left],nums[right]]   
                if temp not in result:      # 应该是这一步耗时比较多
                    result.append(temp)
                break
    return result

print(threeSum([-1,0,1,2,-1,3,-2,4,5,-3,-4,-6]))
