# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        interval = 1
        k = len(lists)
        
        while interval < k:
            for i in range(0,k - interval,interval * 2):
                lists[i] = self.mergeList(lists[i],lists[i + 
                interval])
            interval *= 2

        return lists[0]
    
    def mergeList(self,l1,l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next

            else:
                tail.next = l1
                l1 = l1.next
            
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next

        
    
        
