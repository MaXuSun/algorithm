"""
解决方法：用递归
"""
def letterCombinations(digits):
    """
    time: beats 96.41%
    memory: 85.31%
    """
    if len(digits) == 0:return []
    strs = [None,None,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

    def digit2strs(digits):
        if int(digits) < 10:            # 如果只有一个字符了就直接查表
            return list(strs[int(digits)])
        else:
            result = []
            for first_str in list(strs[int(digits[0])]):        # 先遍历第一个数字对应的字符
                for remainder_str in digit2strs(digits[1:]):    # 再遍历剩余数字对应的字符
                    result.append(first_str+remainder_str)
            return result
    
    return digit2strs(digits)

print(letterCombinations('223'))
            