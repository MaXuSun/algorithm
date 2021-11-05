"""
解题思路：递归+栈
难点：如何去重复？
每次递归的时候，n+1层压入栈的数据要>n层压入栈的数据，这是为了保证栈的数据是有序的
"""
def combinationSum(candidates, target):
    """
    time: beats 5.84%
    memory: beats 10.65%
    """
    result = []
    def combi(candidates,target,stack):
        if target == 0:
            temp = sorted([item for item in stack])
            if temp not in result:
                result.append(temp)
            return None
        if target < 0:
            return None

        for c in candidates:
            stack.append(c)
            combi(candidates,target-c,stack)
            stack.pop()

    combi(candidates,target,[])
    return result

def combinationSum(candidates, target):
    """
    time: beats 40.96%
    memory: beats 92.20%
    """
    result = []
    def combi(candidates,target,stack):
        if target == 0:
            result.append(stack.copy())
            return None
        if target < 0:
            return None

        for i,c in enumerate(candidates):
            if not stack or c >= stack[-1]:
                stack.append(c)
                combi(candidates,target-c,stack)
                del stack[-1]

    combi(candidates,target,[])
    return result

print(combinationSum([10,1,2,7,6,1,5],8))