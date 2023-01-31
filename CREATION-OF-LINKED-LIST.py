class Node:
    def __init__(self,data,next=None):
        self.data= data
        self.next= next
class LinkedList:
    def __init__(self,head=None):
        self.head=head
    def add(self,data):
        new=Node(data)
        if(self.head):
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new
        else:
            self.head=new
    def List(self,first=None):
        self.first=first
        first=self.head
        while(first):
            print(first.data)
            first=first.next
            
obj=LinkedList()
obj.add(20)
obj.add(30)
obj.add(50)
obj.List()
