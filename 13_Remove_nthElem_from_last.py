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
    def RemoveNth(self,n):
        curr=self.head
        count=0
        while(curr is not None):
            count+=1
            curr=curr.next
        if n == count:
            self.head = self.head.next
            return
        remove_elem=count-n
        curr=self.head
        while curr is not None:
            remove_elem -=1
            if remove_elem==0:
                curr.next=curr.next.next
                return
            curr=curr.next
            
LL=LinkedList()
value=input("Enter value to insert in the LL (use space in each Insertion) ").split(" ")
for var in value:
    LL.InsertElem(int(var))
LL.PrintLL()
LL.RemoveNth(5)
LL.PrintLL()


