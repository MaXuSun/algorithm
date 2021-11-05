"""
解题思路：使用两次二分查找法，分别用于查找最左边的和最右边的target
难度：需要控制二分法查找的方向，查找左边时，当target=nums[mid]时，令right=mid-1
    查找右边时，当target=nums[mid]时，令left=mid+1
"""
def searchRange(nums,target):
    """
    time: beats 99.43%
    memory: 95.98%
    """
    def find(nums,target,mode='left'):
        left,right = 0,len(nums)-1
        index = -1
        while left <= right:
            mid = left + (right-left)//2
            if target == nums[mid]: 
                index = mid
                if mode == 'right': # 查找右边
                    left = mid + 1
                elif mode == 'left':    # 查找左边
                    right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        return index
    
    left = find(nums,target)
    right = find(nums,target,'right')
    return [left,right]

print(searchRange([],0))
    
