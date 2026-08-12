class Node:
    def __init__(self, value=None):
      self.data=value
      self.next=None
      self.prev=None
class DoubleLL:
    def __init__(self,head=None):
        self.head=head
    def InsertAtEnd(self,value):
        temp=Node(value)
        if(self.head is None):
            self.head=temp
            return
        t=self.head
        while(t.next is not None):
            t=t.next
        t.next=temp
        temp.prev=t
    def PrintLL(self):
        t=self.head
        while t is not None:
            print(t.data,end="-> ")
            t=t.next
        print("->None")

Obj=DoubleLL()
Obj.InsertAtEnd(90)
Obj.InsertAtEnd(34)
Obj.InsertAtEnd(12)
Obj.PrintLL()
