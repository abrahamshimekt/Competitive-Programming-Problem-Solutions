# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        N = len(lists)
        nums = []
        for linkedList in lists:
            curr = linkedList
            while curr:
                nums.append(curr.val)
                curr = curr.next
        heapify(nums)
        ans = []
        while nums:
            num = heappop(nums)
            ans.append(num)
            heapify(nums)
        def insert(root,value):
            newNode = ListNode(value)
            if not root:
                root = newNode
            else:
                curr = root
                while curr.next:
                    curr = curr.next
                curr.next = newNode
            return root
        def createLinkedList(nums,n):
            root = None
            for i in range(n):
                root = insert(root,nums[i])
            return root
       
         
        return createLinkedList(ans,len(ans))



            
