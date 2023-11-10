class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        q, r = divmod(n, k) 

        result = []
        curr = head

        for i in range(k):
            result.append(curr)
            part_size = q + (i < r)  
            for _ in range(part_size-1):
                if curr:
                    curr = curr.next
            if curr:
                temp = curr.next
                curr.next = None
                curr = temp

        return result
