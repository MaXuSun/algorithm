"""
解题思路：
1. 从头开始遍历，先把空格去掉
2. 读第一个字母，判断是否在"0123456789-+"中，不是的话,return 0
3. 继续遍历，如果先遇到string，就报错，如果遇到int number，就保存，知道遇到非int number
犯的错误：
1. 没有考虑空字符串
2. 没有考虑去掉头部空格后的空字符串
3. 没有考虑多个正负号的情况
"""
def myAtoi(s):
    """
    time: beats 98.63%
    memory: beats 80.88%
    """
    index = 0
    length = len(s)
    strnum = ""

    if length == 0:     # 空串
        return 0

    while index < length and s[index] == " ":   # 读取头部空格
        index += 1

    if index >= length or s[index] not in '0123456789-+':   # 读取剩下的字符串的头部元素，防止多个符号
        return 0
    strnum+=s[index]

    # 读取剩下的数字
    index+=1
    while index < length:
        if s[index] not in '0123456789':
                break
        else:
            strnum+=s[index]
        index+=1

    # 将字符串转化成数字
    result = 0
    for item in strnum:
        if item in '-+':continue
        result = 10*result + int(item)
    
    # 符号限制和数字大小边界限制
    result = -result if strnum[0] == '-' else result
    result = -2**31 if result < -2**31 else result
    result = 2**31-1 if result > 2**31 -1 else result
    return result

print(myAtoi(" "))
