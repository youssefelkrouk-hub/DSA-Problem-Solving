# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head ) :
        slow = head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next
        return slow

# Build 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol=Solution()
new_head=sol.middleNode(head)

# Print the result
curr = new_head
output=[]
while curr:
    output.append(curr.val)
    curr=curr.next
print(output)


