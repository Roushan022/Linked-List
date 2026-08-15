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
    def Rotate_nth(self,n):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=self.head
        count=0
        t=self.head
        while count <n-1:
            t=t.next
            count+=1
        self.head=t.next
        t.next=None
LL=LinkedList()
#value=input("Enter value to insert in the LL (use space in each Insertion) ").split(" ")
# for var in value:
#     LL.InsertElem(int(var))
LL.InsertElem(10)
LL.InsertElem(20)
LL.InsertElem(30)
LL.InsertElem(40)
LL.InsertElem(50)
LL.PrintLL()
LL.Rotate_nth(3)
LL.PrintLL()


