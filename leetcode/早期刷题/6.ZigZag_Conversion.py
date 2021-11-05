"""
解题思路：找规律
对于第一行和最后一行：每隔numRows*2-2个元素取一个
对于其他行：每次取两个元素，在这里分成左右两个元素item_left和item_right,每两个item_left位置相差numRows*2-2
每两个item_right位置相差numRows*2-2，因此找到每个item_left和item_right的关系即可
"""
def convert(s,numRows):
    """
    time: beats 69.15%
    memory: beats 70.68%
    """
    length = len(s)
    if numRows == 1:
        return s
    result = ""
    for j in range(numRows):
        if j == 0 or j == numRows-1:
            for i in range(j,length,numRows*2-2):
                result += s[i]
        else:
            i = j
            while i < length:
                result += s[i]
                if i + 2*(numRows-1-j) < length:
                    result += s[i+2*(numRows-1-j)]
                i += (numRows*2-2)
    return result


print(convert('A',1))