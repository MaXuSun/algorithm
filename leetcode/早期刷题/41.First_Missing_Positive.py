"""
可以多看看
解题思路：You must implement an algorithm that runs in O(n) time and uses constant extra space: 必须使用O(n)的时间复杂度，并且只使用定量的额外空间，说明空间复杂度是O(1)
类似于桶排序的思路，对于每一个整数，我们按照一定的规则放到相应的位置上，最后再去检查如果指定位置的数不存在，即为没有出现的最小正整数。 第i个位置放i+1
类似题目：n个元素的数组，里面的数都是0~n-1范围内的，求数组中反复的某一个元素。没有返回-1, 要求时间性能O(n) 空间性能O(1)
"""
def firstMissingPositive(nums):
    """
    time: beats 47.37%
    memory: beats 47.03%
    """
    length = len(nums)
    for i in range(length):
        """
        nums[i] > 0: 这是因为对于<=0的数，我们不关心
        nums[nums[i] - 1] != nums[i]: 我们只关心>0的数并想将其摆放到正常的位置
        nums[i]<=length: 超过数组长度的数据用不到，因为这个全是负数的话，这个正数是1，可以遍历到，全是正数的话，是len(nums)+1
        """
        while nums[i] > 0 and nums[i]<=length and nums[nums[i] - 1] != nums[i] :
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(length):
            if nums[i] <= 0 or nums[i] != i+1:
                return i+1
        return length+1

print(firstMissingPositive([1,1]))
