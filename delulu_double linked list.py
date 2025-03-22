print('''A single linked list is like''')
print("\n")
print('''[[[prev(data)][data][next(data)]]-->[[[prev(data)][data][next(data)]]''')
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class delulu:
    def __init__(self):
        self.head=None
    
    def traversing_forward(self):
        if self.head is None:
            print("List is empty")
        else:
            print("Forward Traversal:")
            temp=self.head
            while temp is not None:
                
                print(temp.data,end="-->")
                temp=temp.next
    
    def traversing_backwards(self):
        if self.head is None:
            print("list is empty")
        else:
            print("\nBackward Traversal:")
            temp=self.head
            while temp.next is not None: #it has reached the last node
                temp=temp.next
            #In each iteration, it moves printval to the next node by assigning printval.next to printval/           
            while temp is not None: #This loop traverses the DLL from the last node to the first node
            #which means it has reached the beginning of the DLL    
                
                print(temp.data,end="-->")
                temp=temp.prev
    
    def insert_at_begenning(self,data):
        newnode=node(data)
        if self.head is None:
            print("the list is empty")
            self.head=newnode
        else:
            temp=self.head
            # Now the newnode which will be in the place of self.head tht node's next value will be self.head until it's head value is changed
            #and self.head's prev value will be newnode and then current self.head will be given as newnode
            newnode.next=self.head
            temp.prev=newnode
            self.head.prev=newnode
            self.head=newnode
    
    def insert_at_position(self, data, pos):
        newnode = node(data)  # Create the new node with the provided data
    
    # If the list is empty and pos is greater than 1, insertion is invalid
        if self.head is None and pos != 1:
            print("Cannot insert at position", pos, "- the list is empty.")
            return
    
    # If inserting at the first position
        if pos == 1:
            self.insert_at_begenning(data)
        else:
            temp = self.head
        
        # Traverse the list to find the node before the insertion point
        for i in range(pos - 2):
            if temp is None:  # If temp is None, the position is out of bounds
                print("Given position is out of bounds in DLL")
                return  # Exit the method since the position is invalid
            temp = temp.next
        
        # After the loop, check if temp is None (position out of range)
        if temp is None:
            print("Given position is out of bounds in DLL")
            return
        
        # Inserting the new node at the position
        newnode.next = temp.next
        newnode.prev = temp
        temp.next = newnode
        
        # Adjusting the next node's previous pointer, if it exists
        if newnode.next is not None:
            newnode.next.prev = newnode



    def insert_at_end(self,data):
        newnode=node(data)
        if self.head is None:
            print("the list is empty")
            return 
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=newnode
            newnode.prev=temp
        
    def delete_at_begenning(self):
        if self.head is None:
            print("the list is empty")
        else:
            temp=self.head
            self.head=self.head.next # this will change to next node and keep it as head
            self.head.prev=None #after keeping the new head chamging the prev value to none
    
    def delete_at_pos(self, pos):
        if self.head is None:  # If the list is empty
            print("List is empty, cannot delete.")
            return
    
    # Deleting the head node
        if pos == 1:
            self.head = self.head.next
            while self.head is not None:
                self.head.prev = None
            return
    
    # Initialize a temporary pointer to traverse the list
        tempi = self.head
    
    # Traverse to the node just before the position to be deleted
        for i in range(pos - 2):
            if tempi is None:  # If we've reached the end of the list
                print("Position out of range, cannot delete.")
            return
        tempi = tempi.next
    
    # Check if the node at position exists
        if tempi is None or tempi.next is None:
            print("Position out of range, cannot delete.")
            return
    
    # Bypassing the node at position
        to_delete = tempi.next  # Node to be deleted
        tempi.next = to_delete.next
        if to_delete.next is not None:
            to_delete.next.prev = tempi

    

    def delete_at_End(self):
        if self.head is None:
            print("the list is empty")
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None #this will delete the last node in the list
            temp.prev=None

    
# Create a new doubly linked list
dll = delulu()

# Insert nodes at the beginning of the list
dll.insert_at_begenning(10)
dll.insert_at_begenning(20)
dll.insert_at_begenning(30)
dll.insert_at_begenning(40)
dll.insert_at_begenning(50)
dll.insert_at_begenning(29)
dll.insert_at_begenning(21)
dll.insert_at_begenning(22)
dll.insert_at_begenning(24)
# Insert nodes at the end of the list
dll.insert_at_end(100)
dll.insert_at_end(200)
dll.insert_at_end(233)
    # Insert nodes at the end of the list
dll.insert_at_end(40)
dll.insert_at_end(50)
    # Insert nodes at a specific position in the list
dll.insert_at_position(25, 2)
    # Print the list in forward direction
dll.traversing_forward()
    # Print the list in backward direction#dll.traversing_backwards()
    # Delete the node at the beginning of the list
dll.delete_at_begenning()
    # Delete the node at a specific position in the list
dll.delete_at_pos(2)
    # Delete the node at the end of the list
dll.delete_at_End()
    # Print the list in forward direction after deletion
print("\nForward Traversal after deletion:")
dll.traversing_forward()
# Print the list in backward direction after deletion
print("\nBackward Traversal after deletion:")
dll.traversing_backwards()

        
                

        






