"""
构建自动状态机来模拟匹配正则表达式
"""
def isMatch(s,p):
    index1 = 0
    index2 = 0
    while index1 < len(s) and index2 < len(p):
        if s[index1] == p[index2]:
            index1 += 1
            index2 += 1
        else:
            if p[index2].islower():
                if index2 + 1 < len(p) and p[index2+1] == '*':
                    index2 += 1
                else:
                    return False
            elif p[index2] == '.':
                index1 += 1
                index2 += 1
            elif p[index2] == '*':
                if p[index2-1]==s[index1] or p[index2-1] == '.':
                    index1 += 1
                else:
                    index2 += 1
    print(index1,index2)
    while index2 < len(p):
        if p[index2] == '*':
            index2 += 1
        elif index2+1 < len(p) and p[index2+1] == "*":
            index2+=1
        else:
            break
            
    return True if index1 == len(s) and index2 == len(p) else False

print(isMatch('aaa','a*a'))
                