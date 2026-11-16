# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0,head)
        getPrev = dummy

        while True:
            kth = self.getKth(k,getPrev)
            
            if not kth:
                break

            groupNext = kth.next

            prev = groupNext
            curr = getPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tmp = getPrev.next
            getPrev.next = kth
            getPrev = tmp
        return dummy.next 

        


    def getKth(self,k,curr):
        while k > 0 and curr:
            curr = curr.next
            k -=1
        return curr
        
