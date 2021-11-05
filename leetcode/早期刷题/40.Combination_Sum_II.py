"""
解题思路：使用栈+递归+剪枝
和上题不同，这里加了一个限制，要求一个元素只能使用一次，那就需要
1. 在递归的时候，先排序，再只留下candidates的右半部分。
但是只有1限制还不够，不能保证元素重复时，有些层会选择重复的元素，比如 1122567,在第一层两个1，第二层2个2，需要再加一个限制
2. 每次只选重复元素的第一个

"""
def combinationSum2(candidates, target):
    """
    time: beats 23.81%
    memory: beats 92.09%
    """
    candidates.sort()
    result = []
    def combi(candidates,target,stack):
        if target <= 0:
            if target == 0:
                result.append(stack.copy())
            return None

        for i,c in enumerate(candidates):
            if i==0 or c!=candidates[i-1]:
                stack.append(c)
                combi(candidates[i+1:],target-c,stack)
                stack.pop()
    combi(candidates,target,[])
    return result

print(combinationSum2([10,1,2,7,6,1,5],8))

