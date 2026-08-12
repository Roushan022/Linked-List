def InsertAtMid(self,value):
  temp=Node(value)
  if self.head is None:
    self.head=temp
    return
  while(t is not None and t.data!=x):
    t=t.next
  temp.next=t.next
  t.next.prev=temp
  t.next=temp
  temp.prev=t
    
