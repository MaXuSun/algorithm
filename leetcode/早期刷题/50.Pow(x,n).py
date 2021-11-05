"""
解题思路：分成>0的指数，<0的指数和=0的指数
1. 直接暴力法：显然会超时
2. 快速求法：使用分治法求
3. 迭代+快速求法
"""
def myPow(x,n):
    """
    这种暴力解法，会超时
    """
    flag = False
    if n < 0:
        flag = True
        n = -n
    
    result = 1
    for _ in range(n):
        result *= x
    
    return 1/result if flag else result

def myPow(x,n):
    """
    time: beats 62.28%
    memory: 50.23%
    """
    flag = True if n < 0 else False
    n = max(n,-n)

    dictery = {}    # 用于递归的时候剪枝
    dictery[0] = 1

    def fastpow(x,n,dictery):
        print(n)
        if dictery.get(n):
            return dictery[n]
        half = n//2
        y = fastpow(x,half,dictery)
        dictery[half] = y
        dictery[n] = y*y if half * 2 == n else y*y*x
        return dictery[n]
    result = fastpow(x,n,dictery)
    return 1/result if flag else result 
    

def myPow(x,n):
    """
    这个解法是最优解法
    """
    flag = True if n < 0 else False
    n = max(n,-n)
    result = 1
    while n!=0:
        if (n & 1) == 1:
            result *= x
        n = n >> 1
        x = x*x
    return 1/result if flag else result 
        

print(myPow(2,-10))