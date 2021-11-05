"""
两种解题思路，一种是正常的解法
一种是利用python语言的便捷，转成str后再转成int
"""
def reverse(x):
    """
    time: beats 97.50%
    memory: beats 44.23%
    """
    result = 0
    num = -x if x < 0 else x;

    while num > 0:
        temp = num%10
        result = result*10+temp
        num = num//10
    result = -result if x < 0 else result
    if result < -2**31 or result > 2**31-1:
        return 0
    return result

def reverse(x):
    """
    time: beats 71.92%
    memory: beats 11.29%
    """
    num = -x if x < 0 else x;
    strnum = str(num)[::-1]
    result = -int(strnum) if x < 0 else int(strnum)
    if result < -2**31 or result > 2**31-1:
        return 0
    return result
print(reverse(1534236469))