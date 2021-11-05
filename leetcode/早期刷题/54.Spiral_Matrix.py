"""
解题思路：每次打印最外面一圈
"""
def spiralOrder(matrix):
    left,top = 0,0
    right,bottom = len(matrix),len(matrix[0])
    ans = []

    def spiral(matrix,left,right,top,bottom,ans):
        if left > right and left > right:
            return
        for i in range(left,right):
            ans.append(matrix[top][i])
        for i in range(top+1,bottom):
            ans.append(matrix[i][right-1])
        for i in range(right-2,left-1,-1):
            ans.append(matrix[bottom-1][i])
        for i in range(bottom-2,top,-1):
            ans.append(matrix[i][left])
        spiral(matrix,left+1,right-1,top+1,bottom-1,ans)
    spiral(matrix,left,right,top,bottom,ans)
    return ans

print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
