# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialise pointers
        curr_node = head
        prev_node = None

        while (curr_node != None):
            # Reverse current pointer
            next_node = curr_node.next  # Save next node
            curr_node.next = prev_node 

            # Move to next node
            prev_node = curr_node
            curr_node = next_node

        # When curr_node is none, prev is head
        head = prev_node
        return head
        
        
