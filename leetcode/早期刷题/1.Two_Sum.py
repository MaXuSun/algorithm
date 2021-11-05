"""
解题思路：使用一个字典maps存储数据和下标。
然后依次遍历nums,当nums[i]和target-nums[i]都在maps中，则得到所求的下标
"""
def twoSum(nums,target):
    """
    time: beats 93.39%
    memory: beats 22.64%
    """
    maps = {}
    for i,num in enumerate(nums):
        maps.setdefault(num,i)
        j = maps.get(target-num)
        if j is not None and j != i:
            return j,i


if __name__ == '__main__':
    nums = [3,3]
    target = 6
    print(twoSum(nums,target))