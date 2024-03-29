class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int: 
        if index >= self.size:
            return -1
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            return curr.val
        

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        self.size +=1
       
    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(val)
        self.size +=1
       

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        else:
            prev = None
            curr = self.head
            for _ in range(index):
                prev = curr
                curr = curr.next
            new_node = Node(val)
            if not prev:
                new_node = Node(val)
                new_node.next = self.head
                self.head = new_node
            else:
                prev.next = new_node
                prev = prev.next
                prev.next = curr
            self.size +=1
           

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return 
        else:
            prev = None
            curr = self.head
            for _ in range(index):
                prev = curr
                curr = curr.next
            if not prev:
                self.head = self.head.next
            else:
                if not curr:
                    prev.next = curr
                else:
                    prev.next = curr.next
                    curr.next = None
            self.size -=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
