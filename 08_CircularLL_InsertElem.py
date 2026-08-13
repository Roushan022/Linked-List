class Node:
    def __init__(self,info):
        self.data=info
        self.next=None
class CircularLL:
    def __init__(self,head=None):
        self.head=head
    def InsertElem(self,value):
        temp=Node(value)
        if self.head is None:
            self.head=temp
            temp.next=self.head
            return
        t=self.head
        while (t.next is not self.head):
            t=t.next
        t.next=temp
        temp.next=self.head
    def PrintLL(self):
        t=self.head
        while(t.next is not self.head):
            print(t.data,end="->")
            t=t.next
        print(t.data,end="->Head")
LL=CircularLL()
LL.InsertElem(34)
LL.InsertElem(56)
LL.InsertElem(39)
LL.InsertElem(304)
LL.PrintLL()
