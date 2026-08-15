class Node:
    def __init__(self,info):
        self.data=info
        self.next=None

class LinkedList:
    def __init__(self,head=None):
        self.head=head
    
    def InsertElem(self,value):
        temp=Node(value)
        if self.head is None:
            self.head=temp
        else:
            t=self.head
            while(t.next is not None):
                t=t.next
            t.next=temp
    def PrintLL(self):
        t=self.head
        while t is not None:
            print(t.data,end="->")
            t=t.next
        print("None\n")
    
    def ReverseLL(self):
        prev=None
        curr=self.head
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
       
LL=LinkedList()
value=input("Enter value to insert in the LL (use space in each Insertion) ").split(" ")
for var in value:
    LL.InsertElem(int(var))
LL.PrintLL()
LL.ReverseLL()
LL.PrintLL()


