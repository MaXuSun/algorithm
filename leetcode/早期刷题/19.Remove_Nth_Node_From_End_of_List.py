"""
解题思路：使用两个指针，一个先走，一个后走（算是two points的一种变形吧）
出错点：没有设置头指针的话，当n=链表长度，需要特殊考虑
吸取教训：对于链表问题，尽量先使用个空头，可以避免很多麻烦！！！
"""

class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self,head,n):
        """
        time: beats 78.01%
        memory: 91.69%
        """
        Head = ListNode(-1,head)
        p1 = p2 = Head
        for i in range(n):
            p2 = p2.next
        
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return Head.next