# creating a singly linked list

class node:
    def __init__(self,value):
        self.value=value
        self.next=None

class linked_list:

    def __init__(self):
       
        self.head=None
        self.tail=None
        self.length=0

    def append(self,value):
        new=node(value)

        if self.head is None:
            self.head=new
            self.tail=new

        
        else:
            self.tail.next=new
            self.tail=new
        self.length+=1

    

obj=linked_list()
obj.append(10)
obj.append(30)
obj.append(10)
obj.append(30)
print(obj.length)      

