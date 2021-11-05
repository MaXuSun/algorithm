"""
解决思路：很简答的一个栈使用的问题：
    遍历字符串，当栈空或者读入的元素不可以和栈头匹配，就添加到栈中；否则就消除栈头元素
    遍历完毕后，判断栈是否为空。
"""
def isValid(s):
    """
    time: beats 65.83%
    memory: 86.21%
    """
    _stack = []

    def match(s1):
        return True if s1=="()" or s1=="{}" or s1=="[]" else False

    for item in s:
        if len(_stack) == 0 or not match(_stack[-1]+item):
            _stack.append(item)
        else:
            _stack.pop(-1)
    if len(_stack) == 0:
        return True
    else:
        return False

s = "{[]}"
print(isValid(s))