# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l = ListNode(0)
        head = l
        while (l1 or l2):
            x = (l1.val if l1 else 0)
            y = (l2.val if l2 else 0)
            suml = (x+y+carry)
            carry = suml//(10)
            l.next = ListNode(suml%10)
            l = l.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        if carry>0:
            l.next = ListNode(carry)
        return head.next
​
            
