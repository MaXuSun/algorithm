"""
解题思路：使用递归的方法
"""

def generateParenthesis(n):
    """这是我的解法，是有问题的,显然有些情况是没法考虑进去的
    比如："(())(())"
    """
    if n == 1:
        return ['()']
    else:
        result = []
        for item in generateParenthesis(n-1):
            if '({})'.format(item) not in result:
                result.append('({})'.format(item))
            if '(){}'.format(item) not in result:
                result.append('(){}'.format(item))
            if '{}()'.format(item) not in result:
                result.append('{}()'.format(item))

def genrateParenthesis(n):
    """
    想法也是回溯，但是比我刚才的想法更"元"：所有的左括号必然在右括号左边，所以我们先回溯左括号再回溯右括号
    """
    ans = []
    def backtrack(S=[],left=0,right=0):
        if len(S) == 2*n:
            ans.append("".join(S))
            return
        
        if left < n:
            S.append("(")
            backtrack(S,left+1,right)
            S.pop()
        
        if right < left:        # 保证每次append之后，右括号个数要比左括号个数少
            S.append(')')
            backtrack(S,left,right+1)
            S.pop()
        backtrack()
        return ans


def generateParenthesis(n):
    if n == 0:
        return ['']
    result = []
    for c in range(n):
        for left in generateParenthesis(c):
            for right in generateParenthesis(n-1-c):
                result.append('({}){}'.format(left,right))
    return result

print(generateParenthesis(3))

# output

# expected
