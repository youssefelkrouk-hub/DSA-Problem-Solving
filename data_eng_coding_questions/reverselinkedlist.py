class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev=None
        curr=head
        while curr: # in the first loop curr  would be head !! 
            next_curr=curr.next
            curr.next=prev
            prev=curr
            curr=next_curr
        return prev

            

# Build 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = solution() # an instance of the solution clas
new_head = sol.reverseList(head) # or just wa can do this solution().reverseist(head)

# Print the result
curr = new_head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")