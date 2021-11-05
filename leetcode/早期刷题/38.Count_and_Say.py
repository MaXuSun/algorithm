"""
解题思路：使用递归解法
注意点：
当n逐渐增大，得到的字符串越来越长，不能用int表示
"""
def countAndSay(n):
    """
    time: beats 33.23%
    memory: beats 75.57%
    """
    if n==1:
        return '1'
    _str = countAndSay(n-1)
    result = ''
    front = 0
    end = 0
    for s in _str:
        if s != _str[front]:
            result+='{}{}'.format(end-front,_str[front])
            front = end
        end+=1
    if end >= front:
        result+='{}{}'.format(end-front,_str[front])
    return result

print(countAndSay(6))
