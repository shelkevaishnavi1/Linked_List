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
    
#insert at first place    

    def prepend(self,value):
        new=node(value)

        if self.head is None:
            self.head=new
            self.tail=new
        
        else:
            new.next=self.head
            self.head=new

        self.length += 1

#get the element by index

    def get(self,index):
        current=self.head
        for i in range(index):
            current=current.next
        return current.value
    

obj=linked_list()
obj.append(100)
obj.append(10)
obj.append(30)
obj.append(60)
obj.append(80)

print(obj.get(3))



