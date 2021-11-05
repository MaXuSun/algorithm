"""
从高向低，每次将数据减去最高的数值
其他解法：
也可以不用减，用整除和取余
"""
def intToRoman(num):
    """
    time: beats 77.13%
    memory: 58.76%
    """
    integer = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    romans = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    i2r = dict(zip(integer,romans))
    result = ""
    while num > 0 :
        for item in integer[::-1]:
            if num >= item:
                result+=i2r[item]
                num -= item
                print(num,item,i2r[item])
                break
    return result

print(intToRoman(3423))

