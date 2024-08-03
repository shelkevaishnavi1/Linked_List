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

obj=linked_list()
obj.append(25)
obj.append(45)
obj.append(55)
obj.append(65)
obj.append(75)
obj.append(45)
obj.insert(2,100)
print(obj.display())
print(obj.length)