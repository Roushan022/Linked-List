class Node:
    def __init__(self,info):
        self.data=info
        self.next=None
class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head
    def InsertElem(self,value):
        temp=Node(value)
        if(self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp
        else:
            self.head=temp
    def InsertAtBeg(self,value):
        temp=Node(value)
        temp.next=self.head
        self.head=temp
    def PrintLL(self):
        count=0
        t1=self.head
        while(t1.next!=None):
            print(t1.data,end="->")
            count+=1
            t1=t1.next
        print(t1.data,end="->None")
        count+=1
        print("\n",count)
    def SearchElem(self,x):
        t1=self.head
        found=False
        while(t1!=None):
            if(t1.data==x):
                print(f"Found {x}")
                found=True
                break
            t1=t1.next
        if not found:
            print(f"Not Found {x}")
LL=SinglyLinkedList()
value=input("Enter your input:- ").split()
for var in value:
    LL.InsertElem(var)
value_1=input("enter the value to insert at beg:- ")
LL.InsertAtBeg(value_1)
LL.InsertElem(89)
LL.PrintLL()
LL.SearchElem(89)
LL.SearchElem(100)



