   def InsertAtMid(self,value,x):
        temp=Node(value)
        if self.head==None:
            print("Linked List is empty ")
            return
        else:
            t=self.head
            while(t.next!=self.head):
                if t.data==x:
                    temp.next=t.next
                    t.next=temp
                    return
                t=t.next
    def PrintLL(self):
        t=self.head
        while(t.next is not self.head):
            print(t.data,end="->")
            t=t.next
        print(t.data,end="->Head")
