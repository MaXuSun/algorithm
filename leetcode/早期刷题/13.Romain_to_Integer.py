"""
解题思路：遍历字符串，每次遍历向后探一位，如果这俩个字符在roman数字中，直接处理2位，如果不在，处理一位
"""
def romanToInt(s):
    """
    time: beats 83.80%
    memory: beats 57.82%
    """
    integer = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    romans = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    i2r = dict(zip(romans,integer))
    result = 0
    i = 0
    while i < len(s):
        if s[i] == 'I' and i+1 < len(s) and s[i+1] in ['V','X']:
            result += i2r[s[i:i+2]]
            i += 2
        elif s[i] == 'X' and i+1 < len(s) and s[i+1] in ['L','C']:
            result += i2r[s[i:i+2]]
            i += 2
        elif s[i] == 'C' and i+1 < len(s) and s[i+1] in ['D','M']:
            result += i2r[s[i:i+2]]
            i += 2
        else:
            result += i2r[s[i]]
            i+=1

    return result

print(romanToInt( "MCMXCIV"))