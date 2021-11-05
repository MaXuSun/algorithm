"""
解题思路：使用递归的方式,所有递归的题目都可以使用栈来模拟
递归：注意终止条件
"""
def permute(nums):
    """
    这种是使用递归的方法
    time: beats 22.56%
    memory: 71.02%
    """
    if len(nums)==1:
        return [nums]
    
    result = []
    for i,num in enumerate(nums):
        temp = permute(nums[:i]+nums[i+1:])
        for item in temp:
            result.append([num]+item)
    return result

print(permute([1,2,3,4,5]))