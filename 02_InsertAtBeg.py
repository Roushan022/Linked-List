class Node:
    def __init__(self, info, next=None):
        self.data=info
        self.next=next
class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head
    def InsertAtBeg(self, value):
        temp=Node(value)
        temp.next= self.head
        self.head = temp
    def printLL(self):
        t1=self.head
        while(t1.next!=None):
            print(t1.data,end="-> ")
            t1=t1.next
        print(t1.data,end="->None ")
LL=SinglyLinkedList()
value=input("Enter the valuess:- ").split(" ")
for var in value:
    LL.InsertAtBeg(var)
LL.printLL()
