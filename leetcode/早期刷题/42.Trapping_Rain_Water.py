"""
解题思路：使用动态规划
对于每个元素，我们要找到它左边的最大高度leftmax,右边的最大高度rightmax，则该元素接到的雨水就是：min(leftmax,rightmax)-item
因此我们需要找每个元素的左边最大高度和右边最大高度：使用动态规划查找。做动态规划需要直到状态转移方程：
1. 当 1<= i <= n-1时，leftMax[i] = max(leftMax[i-1],height[i])
2. 当 0<= i <= n-2时，rightMax[i] = max(rightMax[i+1],height[i])
"""
def trap(height):
    if not height:
        return 0
    length = len(height)
    leftmax = [height[0]] + [0]*(length-1)
    rightmax = [0]*(length-1) + [height[length-1]]

    for i in range(1,length):
        leftmax[i] = max(leftmax[i-1],height[i])
    
    for i in range(length-2,-1,-1):
        rightmax[i] = max(rightmax[i+1],height[i])
    
    result = sum([min(leftmax[i],rightmax[i])-height[i] for i in range(length)])
    return result

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))


"""
解题思路：使用stack来解决，每次都往栈里压元素，如果当前遇到的元素>=栈顶，就用当前元素，栈顶和栈下一个元素计算一次，并弹出栈顶元素。直到遍历完毕
"""
def trap(height):
    ans = 0
    stack = list()
    n = len(height)
    
    for i, h in enumerate(height):
        print(stack)
        while stack and h > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            left = stack[-1]
            currWidth = i - left - 1
            currHeight = min(height[left], height[i]) - height[top]
            ans += currWidth * currHeight
        stack.append(i)
    return ans

# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

"""
解题思路：使用两个指针的方法
"""

def trap(height):
    leftmax = height[0]
    rightmax = height[-1]
    left,right = 0,len(height)-1
    result = 0

    while left < right:
        # print(height[left],height[right])
        if height[left] < height[right]:            # 因为先执行这个，所以每次这个判断里面 leftmax < rightmax
            if height[left] < leftmax:
                result += leftmax - height[left]
            else:
                leftmax = height[left]  
            left += 1
        else:                                       # 同样在这个循环里面，rightmax < leftmax
            if height[right] < rightmax:
                result += rightmax - height[right]      # 这里不能使用min(leftmax,rightmax)，因为如果上一次循环left位置增加了水，如果height[left+1]==height[right]，那就来不及更新leftmax，直接跳到68行这个else里面了
            else:
                rightmax = height[right]
            right -= 1
    return result
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
