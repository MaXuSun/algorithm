"""
解题思路：
这是一个常见的题目，主要思想是对两个数组遍历，每次比较取出最小的那个
直到遍历到中间的元素，就停止。
"""
def findMedianSortedArrays_v1(nums1, nums2):
    """
    time: beats 39.21%
    memory: 54.49%
    """
    len1,len2 = len(nums1),len(nums2)
    if (len1+len2)%2 == 0:
        median2 = (len1+len2)//2
        median1 = median2-1
    else:
        median1 = median2 = (len1+len2)//2
    
    result = 0
    cont = 0
    indx1 = 0
    indx2 = 0
    while True:
        if indx1 < len1 and indx2 < len2:
            if nums1[indx1] < nums2[indx2]:
                cont+=1
                indx1+=1
                now_nums = nums1
                now_indx = indx1
            else:
                cont+=1
                indx2+=1
                now_nums = nums2
                now_indx = indx2
        elif indx1 >= len1:
            indx2 += 1
            cont+=1
            now_nums = nums2
            now_indx = indx2
        elif indx2 >= len2:
            indx1 += 1
            cont+=1
            now_nums = nums1
            now_indx = indx1

        print(cont,now_nums,now_indx)
        if cont-1 == median1:
            result+=now_nums[now_indx-1]
        if cont-1 == median2:
            result += now_nums[now_indx-1]
            break
    return result/2

def findMedianSortedArrays(nums1, nums2):
    """
    time: beats 94.22%
    memory: 54.49%
    """
    len1,len2 = len(nums1),len(nums2)
    if (len1+len2)%2 == 0:
        median2 = (len1+len2)//2
        median1 = median2-1
    else:
        median1 = median2 = (len1+len2)//2
    
    result = 0
    index1 = index2 = 0
    for i in range(len1+len2+1):
        if index1 >= len1:
            now_data = nums2[index2]
            index2 +=1
        elif index2 >= len2:
            now_data = nums1[index1]
            index1 += 1
        elif nums1[index1] < nums2[index2]:
            now_data = nums1[index1]
            index1 += 1
        elif nums1[index1] >= nums2[index2]:
            now_data = nums2[index2]
            index2 += 1
        if i == median1:
            result += now_data
        if i == median2:
            result += now_data
            break
    return result/2
        

nums1 = [2,3]
nums2 = [1]
print(findMedianSortedArrays(nums1,nums2))