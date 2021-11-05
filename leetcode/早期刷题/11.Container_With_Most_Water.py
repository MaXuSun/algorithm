"""
解题思路：
v1: 动态规划问题
对于一个数组中height[i,j]水的最大值可以表示为三个方面的最大值：
a. (j-i)*min(height[i],height[j])
b. height[i+1,j]
c. height[i,j-1]

v2: 如果面积最大h[i,j]最大，则不存在k,k<i 使得 h[k] > h[i]，同时不存在k,k>j使得h[k] > h[j]
基于上面，我们从外向内收缩面积，每次把短的那个边界向内收缩
"""
def maxArea_v1(height):
    """
    这种写法时间超时
    """
    if len(height) == 2:
        return min(height)
    return max(maxArea_v1(height[1:]),maxArea_v1(height[:-1]),min(height[-1],height[0])*(len(height)-1))

def maxArea(height):
    """
    time: beats 66.82%
    memory: beats 55.38%
    """
    left = 0
    right = len(height) - 1
    result = 0
    while left < right:
        result = max(result,(right-left)*min(height[left],height[right]))
        if height[left] < height[right]:
            left+=1
        else:
            right-=1
    return result



print(maxArea([1,8,6,2,5,4,8,3,7]))