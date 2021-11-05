"""
解题思路：
1. 使用两个指针，前一个指针先走2步，然后交换后一个指针的下一个节点和前一个指针指向的节点
2. 使用递归的方法，前两个交换后，后面的可以看成一个字串交换的问题。
注意：设置头指针
"""
class ListNode:
    def __init(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs_v1(self,head):
        """
        time: beats 86.91%
        memory: 15.78%
        """
        Head = ListNode(-1,head)
        p1 = p2 = Head
        for i in range(2):
            if p2.next is None:
                return Head.next
            else:
                p2 = p2.next
        while p2:
            p1.next.next = p2.next
            p2.next = p1.next
            p1.next = p2
            
            p2 = p2.next
            
            if p2 is None or p2.next is None:
                break
            p2 = p2.next.next
            p1 = p1.next.next
        return Head.next
    
    def swapPairs_v2(self,head):
        """
        time: beats 66.20%
        memory: 15.78%
        """
        if head is None or head.next is None:           # 如果遇到空子链表或者单个节点的子链表直接返回
            return head
        # 交换head和head.next节点
        p1 = head.next              
        head.next = self.swapPairs(p1.next)
        p1.next = head
        return p1
        
