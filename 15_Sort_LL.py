def SortLL(self):
        if self.head is None:
            return
        t1=self.head
        while(t1.next is not None):
            t2=t1.next
            while(t2 is not None):
                if t1.data> t2.data:
                    t1.data,t2.data=t2.data,t1.data
                t2=t2.next
            t1=t1.next
