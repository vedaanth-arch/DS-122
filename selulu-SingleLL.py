class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class selulu:
    def __init__(self):
        self.head=None 

    def insert_at_begenning(self,data): #function to insert element at start of LL
        newnode=node(data) #creating a node to insert at start of LL
        if self.head is None: #here the conditon is checking is tht no elements are there in the LL
            print("Linked list is empty")
            self.head=newnode
        else:
            newnode.next=self.head #new node point to the current first node in the list 
            self.head=newnode      #the new node inserted is inseted and now the head

    '''the steps to insert at end is
    (a).traversing the list till end or it's next value isn't none
    (b).taking a temp=self.head to keep the changed values 
    (c).keeping a loop until it reaches it's end 
    (d).assigning the temp.next i.e., end element's address part to newnode address part which will overlap the data and the new node
    will be the  last element of the list '''

    def insert_at_END(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        #now to inset at end transver till end and then insert
        else:
            tempp=self.head #taking a temporary variable 
            while tempp.next is not None: #traversing done till it reaches end
                temp=tempp.next #like a loop to continue the  traversal
                #now temp is pointing to the last node in the list
            tempp.next=newnode # Set the next of the last node to the new node
    

    '''To insert at a postion 
    (a).firstly check for position of 0 to inset at begining 
    (b).a temporary variable for self.head
    (c).a loop is given for traversing over the list until the given pos value's before value is found i.e., (pos-1)
    (d).then checking if the position is out of range 
    (e).'''
    def inser_at_position(self,data,pos):
        New_Node = node(data)
        # temp is the temporary pointer which is used to traverse the linked list
        temp = self.head
        # if the position is 0 then the new node is inserted at the beginning of the linked list
        if(pos==0):
            self.insert_at_begenning(data)
        else:
            # traversing the linked list till the position is reached
            for i in range(pos-1):
                # if the position is out of range of the linked list then print an error message
                if(temp is None):
                    print("Invalid position. List does not have that many nodes")
                    return
            
                temp = temp.next
            # New_Node.next is the pointer to the next node which is the node at the position
            temp.next=New_Node.next #the before element's next value is set to new node's next position 
            # temp.next is the pointer to the new node which is inserted at the position
            temp.next = New_Node # the  new node is inserted at the position
    
    def delete_at_begenning(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next #  the head is updated to the next node of the head which is the second node in the list

    def delete_at_END(self):
        if self.head is None:
            print("List is empty")
        else:
            tep=self.head
            # traversing the linked list till the second last node is reached
            if tep.next is None:
                self.head=None
                 #This condition ensures that you are traversing through the linked list node by node until you reach the last node.
               #temp.next.next =second last element
               #temp.next
                # updating the next pointer of the second last node to None
            else:
                while tep.next.next is not None:
                    tep=tep.next 
            tep.next=None
    
    def delete_at_pos(self,pos):
        tempi=self.head
        if  self.head is None:
            print("List is empty")
        
        if pos==0:
            self.head=self.head.next
            return
                #traversing to reach till the 2nd last position of pos given
        for i in range(pos-1):
            if tempi is None or tempi.next is None:  # Check if the position is out of bounds
                print("Invalid position. List does not have that many nodes")
            tempi=tempi.next #bypassing 
       # If the node to be deleted doesn't exist
        if tempi.next is None:
            print("Invalid position. List does not have that many nodes")
        
    # Bypass the node to delete it
        tempi.next = tempi.next.next


    def diplay(self):
        temp=self.head
        if self.head is None:
            print("linked list is empty")
        print("node",end="")
        while temp:
            print("-->",temp.data,end=" ")
            temp=temp.next # temp is moved to the next node
        print()
    
obj=selulu()
obj.head=node("1")
e2=node("2")
e3=node("3")
e4=node("4")
e5=node("5")
e6=node("6")
e7=node("7")
obj.head.next=e2
e2.next=e3
e3.next=e4
e4.next=e5
e5.next=e6
e6.next=e7
e7.next=None
obj.diplay()












