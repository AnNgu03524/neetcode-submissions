# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        nodeSet = set({})

        while(curr != None):
            if curr in nodeSet:
                return True
            nodeSet.add(curr)
            curr = curr.next
        return False

        # Keep a set tracking what we have already stored and by its index
        # If a node has same .value and .next, is it considered the same node?


        