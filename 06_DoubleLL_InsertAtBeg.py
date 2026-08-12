def InsertAtBeg(self,value):
        temp=Node(value)
        if self.head is None:
            self.head=temp
            return
        temp.next=self.head
        self.head.prev=temp
        self.head=temp
