"""
解题思路：先将图片按照对角线对称，然后按照中轴线对称
对角线对称：交换：A(i,j)和A(j,i)
中轴线对称: 交换: A(i,j)和A(n-1-i,j)
"""

def rotate(matrix):
    """
    time: beats 12.66%
    memory: beats 82.28%
    """
    length = len(matrix)
    """按照对角线交换"""
    for row in range(length):
        for col in range(length):
            # 这里先把每一行对角换正确，然后再中轴对称，放在同一行可以节省时间
            if col >= row+1:
                matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]
            if col >= length//2:
                matrix[row][col],matrix[row][length-1-col] = matrix[row][length-1-col],matrix[row][col]

matrix = [[1,2],[3,4]]
rotate(matrix)
print(matrix)

