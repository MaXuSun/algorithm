def isPalindrome(x):
    """
    最简单的版本，使用python语言的简便性
    time: beats 69.37%
    memory: beats 76.58%
    """
    return True if str(x) == str(x)[::-1] else False

def isPalindrome(x):
    """
    这个想法是将x翻转，但是翻转后可能会比int大。下面解决方法很妙：
    翻转一半，通过比较x 和 翻转数据的大小来判断是否翻转了一半
    time: beats 69.37%
    memory: beats 48.41%
    """
    if x < 0 or (x%10 == 0 and x !=0): return False
    result = 0
    while x > result:
        result = result*10 + x%10
        x //= 10
    return True if x == result or x == result//10 else False

print(isPalindrome(10))
    