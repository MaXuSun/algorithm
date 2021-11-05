"""
解题思路：使用一个优先队列维护每个列表的头元素，不断选择最小的，直到所有的队列都是空的
遇到的问题：python的优先队列，可以存入元组，但是在排序的时依次按照元组中元素大小排序，因为ListNode没有实现比较函数，所以这里额外用了一个list来存储头
        也就是：理想的优先队列元素：(val,head ListNode)，实际上的元素：(val,index of head ListNode in lists)
"""
import heapq
class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self,lists):
        """
        time: beats 75.97%
        memory: beats 9.76%
        """
        head = ListNode(0)
        if lists is None:
            return None
        p = head
        head_lists = [_list for _list in lists if _list is not None]                                        # 一个list用于存所有的非空lists
        heap_head = [(_list.val,index) for index,_list in enumerate(head_lists) if _list is not None]       # 元素为元组，元组第一个值为链表头元素的值，第二个值为链表在head_lists中的位置

        heapq.heapify(heap_head)
        while len(heap_head) != 0:
            # print(heap_head)
            top = heapq.heappop(heap_head)
            p.next = ListNode(top[0])
            p = p.next

            top_next_p = head_lists[top[1]].next
            if top_next_p is not None:
                heapq.heappush(heap_head,(top_next_p.val,top[1]))
                head_lists[top[1]] = head_lists[top[1]].next

        return head.next
            

if __name__ == '__main__':
    pass
