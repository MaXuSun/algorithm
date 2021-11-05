"""
解题思路：使用KMP或者暴力解法
"""
def strStr(haystack,needle):
    if len(needle) == 0:return 0
    for i in range(len(haystack)):
        tempi = i
        for j in range(len(needle)):
            if tempi >= len(haystack):
                return -1
            if haystack[tempi] == needle[j]:
                tempi += 1
            else:
                break
        else:
            return i
    else:
        return -1

print(strStr('aaa','aaaaaa'))

