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
        while t.next is not self.head:
            t=t.next
        t.next=temp
        temp.next=self.head

        #1st approach
    def Count(self):
        count=1
        t=self.head
        while(t.next is not self.head):
            count+=1
            t=t.next
        print(f"The length of the linked List {count}") 

        # 2nd aapproch
    def count(self):
        count=0
        t=self.head
        while True:
            count+=1
            t=t.next
            if t is self.head:
                break
        print(count)
LL=CircularLL()
LL.InsertElem(56)
LL.InsertElem(34)
LL.InsertElem(78)
LL.InsertElem(90)
LL.Count()
LL.count()

    
