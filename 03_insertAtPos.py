 def InsertAtPos(self,value,pos):
        temp=Node(value)
        t1=self.head
        while(t1.next!=None and pos>1):
            pos=pos-1
            if pos==1:
                temp.next=t1.next
                t1.next=temp
            t1=t1.next
