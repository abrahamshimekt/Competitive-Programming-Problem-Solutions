# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        meet = False

        # this problem is solved using floyed's cycle detection algorithm and 
        # what floyed says is that if the fast hare and the slow tortoise meet some where in a cycle
        # of race, the distance to where they meet to the cycle of the race begins is equal to the distance between
        # start of the race to the cycle begins.
        # the fist phase what we need now is find the where the hare and the tortoise meet
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meet = True
                break
        # if the toroise and the hare does not meet meaning there is not cycle in the race
        # so there is not point in the race where the cycle begins
        if not meet:
            return None
        # if they meet sometime in the race that means there is a cycle ,so that we need know where the cycle beigns
        # so to find the where the cycle begins , we need to use floyed's method
        else:
            slow = head
            while slow != fast:
                fast = fast.next
                slow = slow.next
            return slow

