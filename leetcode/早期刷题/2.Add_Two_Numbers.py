"""
解题思路：先同时遍历两个链表，再遍历长的那个链表。使用一个变量来存储进位
技巧：遍历链表时，先初始化一个空的头指针。
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    """
    time: beats 70.66%
    memory: beats 70.10%
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        p = result
        flag = 0

        while l1 and l2:                    # 同时遍历两个链表
            flag += (l1.val+l2.val)
            p.next = ListNode(flag%10)
            p = p.next
            flag //=10
            l1 = l1.next
            l2 = l2.next

        """遍历长的链表"""
        llong = l1 if l2 is None else l2
        while llong:
            flag += llong.val
            p.next = ListNode(flag%10)
            p = p.next
            flag //= 10
            llong = llong.next
        """处理进位"""
        if flag > 0:
            p.next = ListNode(flag)
            p = p.next
        return result.next

if __name__ == '__main__':
    pass