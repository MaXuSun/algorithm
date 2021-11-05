"""
解题思路：链表常规题，直接对两个链表遍历，每次取值最小的那个即可
"""
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self,l1,l2):
        """
        time: beats 52.43%
        memory: beats 31.02%
        """
        head = ListNode(-1)
        p = head
        while l1 or l2:
            if not l1:
                temp = l2.val
                l2 = l2.next
            elif not l2:
                temp = l1.val
                l1 = l1.next
            else:
                if l1.val > l2.val:
                    temp = l2.val
                    l2 = l2.next
                else:
                    temp = l1.val
                    l1 = l1.next
            
            p.next = ListNode(temp)
            p = p.next
        
        return head.next