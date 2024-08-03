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

    def pop_first(self):

        if self.length is None:
            return None
        pop_node=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            pop_node.next=None
        self.length -=1
        return pop_node


    def traverse(self):

        current=self.head
        while current:
            print(current.value)
            current=current.next
        
    def pop_last(self):


        
      
        if self.length ==0:
            return None
        pop_element=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.head
                    
        while temp.next is not self.tail:
            temp=temp.next
        self.tail=temp
        temp.next=None
        self.length -=1
        return pop_element
    
    def pop_random(self,index):
        pass


      
            

    

obj=linked_list()
obj.append(10)
obj.append(30)
obj.append(50)
obj.append(30)
obj.traverse()
print("after poping the last element")

obj.pop_last()
obj.traverse()
     