"""
解题思路：写两个函数，分别处理字符串乘和加
其中乘是1位乘多位，加是多位想加
"""
def multiply(num1,num2):
    """
    time: 5.13%
    memory: 80.87%
    """
    def one_multiply(num1,num2,a):
        """假设num2也是int"""
        result = ""
        flag = 0
        for s in num1[::-1]:
            s_num = int(s)
            temp = s_num * num2 + flag
            result+=str(temp%10)
            flag = temp//10
        if flag:
            result += str(flag)
        result = result[::-1] + '0'*a
        return result
    
    def add_multiply(num1,num2):
        """假设num1和num2是翻转的"""
        result = ""
        flag = 0
        for i,s in enumerate(num1):
            s_num = int(s)
            num2_num = 0 if i >= len(num2) else int(num2[i])
            temp = s_num+num2_num+flag
            result += str(temp%10)
            flag=temp//10
        if flag > 0:
            result += str(flag)
        return result[::-1]
    
    result = ""
    for i,num in enumerate(num2[::-1]):
        temp = one_multiply(num1,int(num),i)
        result = add_multiply(temp[::-1],result[::-1])

    index = 0
    while index < len(result) and result[index] == '0':
        index+=1
    result='0' if index == len(result) else result[index:]
    return result
print(multiply('2','3'))


