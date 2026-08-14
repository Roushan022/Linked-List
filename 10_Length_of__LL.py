class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next
class LinkedLL:
    def __init__(self, head=None):
        self.head = head

    def InsertElem(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        temp = Node(value)
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = temp
    def Count(self):
        count = 0
        t = self.head
        while t is not None:
            count += 1
            t = t.next
        print(f"Lenght of the Linked List is {count}")
        return


LL = LinkedLL()
LL.InsertElem(45)
LL.InsertElem(56)
LL.InsertElem(54)
LL.InsertElem(90)
LL.Count()
