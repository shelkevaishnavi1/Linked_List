class node:

    def __init__(self,value) :
        self.value=value
        self.next=None

class linked_list:

    def __init__(self) :
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

    def display(self):

        temp=self.head
        result=""

        while temp is not None:
            result += str(temp.value)

            if temp.next is not None:

                result+="->"

            temp=temp.next
        return result 
    
#insert at random place place    

    def insert(self,index,value):

            new=node(value)
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            new.next=temp.next
            temp.next=new 
            self.length+=1

    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next


obj=linked_list()
obj.append(70)
obj.append(60)
obj.append(20)
obj.append(10)
obj.append(30)
obj.append(40)
obj.traverse()
