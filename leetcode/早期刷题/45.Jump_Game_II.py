"""
解题思路：使用递归
递归终止条件：
    1. 到达
        1. 0，但是在结尾
        2. 非0，但是可以到达结尾
    2. 跳不动了：0，且不在结尾
https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/
"""

def jump(nums):
    depths = [-1] * len(nums)

    def jump1(nums,depth,depths,index):

        if depths[index] != -1:
            return depths[index]
        if nums[0] != 0 and nums[0]+1 >= len(nums): # 成功到达
            depths[index] = depth + int(len(nums)!=1)
            return depths[index]
        if nums[0] == 0:
            if len(nums) == 1:  # 成功到达
                depths[index] = depth
                return depths[index]
            else:               # 跳不动了
                return 10001
        
        result = []
        for i in range(1,nums[0]+1):
            dep = jump1(nums[i:],depth,depths,i+index)
            result.append(dep)
        depths[index] = min(result) + 1
        return depths[index]

    jump1(nums,0,depths,0)
    return depths[0]

print(jump([1]))

"""
注意：上面的解法在有些测试用例中依然会超时，这里使用其他解法
"""

"""
使用贪心算法：每次找当前步和下一步能跳的最远的选择
"""

def jump(nums):
    """
    time: beats 53.36%
    memory: 97.83
    """
    end = 0
    maxposition = 0
    steps = 0
    for i in range(len(nums)-1):
        maxposition = max(maxposition,nums[i]+i)        # 每一个范围能够跳跃的最大范围
        if i == end:        # 当我遍历到上一次的边界时，此时maxposition存储的为上一次范围可跳的最大范围
            end = maxposition
            steps += 1
    return steps
print(jump([2,3,1,1,4]))
