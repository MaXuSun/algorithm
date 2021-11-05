"""
从优化角度来看，依次使用更好的算法。
v1 and v2:使用暴力法，在编写时已经加了一些小技巧，要求最长子串，我就从最长向最短遍历，由此可以省去短串的时间
v3： 使用动态规划,暂时没有实现
v4: Manacher 算法，暂时没有实现
"""

def isPalindromic(s):
    length = len(s)
    for i in range(length):
        if s[i] != s[length-1-i]:
            return False
    return True
def longestPalindrome_v1(s):
    """
    这个实现方法是暴力法，在leetcode中超时
    """
    length = len(s)
    for sublen in range(length,0,-1):
        for start in range(length):
            if start + sublen > length:
                break
            # if s[start:start+sublen] == s[start:start+sublen][::-1]:
            if isPalindromic(s[start:start+sublen]):
                return s[start:start+sublen]

def longestPalindrome_v2(s):
    """
    在判断回文的时候用时太长，这里改进判断回文的方法，勉强被接受
    time: beats 9.97%
    memory: 38.39%
    """
    length = len(s)
    for sublen in range(length,0,-1):
        for start in range(length):
            if start + sublen > length:
                break
            if s[start:start+sublen] == s[start:start+sublen][::-1]:
                return s[start:start+sublen]

print()


    

