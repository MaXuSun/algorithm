"""
解题思路：首先想到的是使用暴力解法
使用一个hash来标记数据是否有重复的
"""

def isValidSudoku(board):
    """
    time: beats 86.51%
    memory: 42.75%
    """
    # 先遍历行
    start = ord('0')
    for i in range(9):
        hash_temp = [0]*10
        for j in range(9):
            char = ord(board[i][j])-start
            if char <= 9 and char > 0:
                if hash_temp[char] == 1:
                    return False
                else:   
                    hash_temp[char] = 1
                
    # 再遍历列
    for j in range(9):
        hash_temp = [0]*10
        for i in range(9):
            char = ord(board[i][j])-start
            if char <= 9 and char > 0:
                if hash_temp[char] == 1:
                    return False
                else:   
                    hash_temp[char] = 1
    
    # 再遍历小9格
    for l_i in range(0,9,3):
        for l_j in range(0,9,3):        # 外两层是以小9格为单位遍历
            hash_temp = [0] * 10
            for i in range(3):  # 内两层是遍历小9格
                for j in range(3):
                    char = ord(board[l_i+i][l_j+j])-start
                    # print(l_i,l_j,l_i+i,l_j+j,board[l_i+i][l_j+j])
                    if char <= 9 and char > 0:
                        if hash_temp[char] == 1:
                            return False
                        else:
                            hash_temp[char] = 1
            
    return True
