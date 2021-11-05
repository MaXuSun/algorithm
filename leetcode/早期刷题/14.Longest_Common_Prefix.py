"""
解题思路：同时遍历多个str
注意点：有的str可能是空串
错误原因：第一个字符串为空串没有考虑到
"""
def longestCommonPrefix(strs):
    """
    time: beats 82.39%
    memory: beats 55.14%
    """
    result = ""
    index = 0
    while True:
        if index >= len(strs[0]):return result  # 这里因为我们使用第一个字符串，所以这里也要表示判断一下
        temp = strs[0][index]
        for _str in strs:
            if index >= len(_str) or _str[index] != temp:
                return result
        else:
            result += temp
            index += 1
strs = ["a"]
print(longestCommonPrefix(strs))

            
