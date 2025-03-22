print("CIRCULAR SINGLE LINKED LIST")
print('''[[[data1][next(data2)]]-->[[[data2][next(data3)]]-->[[[data3][next(data1)]''')

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CSLL:
    def __init__(self):
        self.head=None

    def Print(self):
        #now travesing from 2nd element bcz if 2nd one doesn't eixts then the 1st one prints of
        temp=self.head.next
        print(self.head.data)
        while temp!=self.head: #here a conditon is checked if there is only one element and traverse from tht
            print(temp.data)
            temp=temp.next

    def insert_at_beg(self,data):
        newnode=node(data)
            #1.checking if the list is empty or not if empty then setting the newnode as head
            #2.traversing till end
        if self.head is None:
            print("ll is empty")
            self.head=newnode
            newnode.next=newnode
        else:
            temp=self.head
            while temp.next is not self.head:
                temp=temp.next
            temp.next=newnode #here the temp is at data3 node and temp.next will be 'next(data1)'
            #here we are keeping the datapart of newnode and declaring the self.head as newnode and [[newnode][newnode.next]],
            #here the newnode is inserted after data3 node and now the data1's next value shuld be updated to newnode's next value
            
            newnode.next=self.head
            self.head=newnode

    def insert_at_end(self,data):
        newnode=node(data)
        #1.checking if the list is empty or not if empty then setting the newnode as head
            #2.traversing till end
        if self.head is None:
            print("ll is empty")
            self.head=newnode
            newnode.next=newnode#tht newnode's next shuld point to newnode if only it exists
        else:
            temp=self.head
            while temp.next is not self.head:
                temp=temp.next
            #here temp is at data3 and it's next value is given as newnode(which stores the path of newnode)
            #and newnode's next is stored as self.head
            temp.next=newnode
            newnode.next=self.head

    def insert_at_pos(self, data, pos):
        new_node = node(data)  # Create a new node with the given data
        if pos < 0:  # Check if position is valid
            print("Invalid position")
            return    
        if pos == 0:  # Insert at the beginning
            if self.head is None:  # If the list is empty
                print("The list is empty. Adding the first node.")
                self.head = new_node  # Set the new node as the head
                new_node.next = new_node  # Point new node to itself (circular)
            else:  
            # Find the last node to complete the circular link
                last_node = self.head
                while last_node.next != self.head:  # Loop until reaching the last node
                    last_node = last_node.next
            
                new_node.next = self.head  # Link new node to the current head
                self.head = new_node  # Update head to the new node
                last_node.next = self.head  # Point last node to new head to maintain circular link

        else:  # Insertion at a specific position
            current = self.head
            count = 0
        # Traverse to the position just before the desired one
            while count < pos - 1 and current.next != self.head:
                current = current.next
                count += 1
        
            if count == pos - 1:  # Check if position is valid in the list
                new_node.next = current.next  # Link new node to the next node
                current.next = new_node  # Link current node to the new node
            else:
                print("Position out of range")

    def delete_at_beg(self):
        if self.head is None:
            print("ll is empty")
        else:
            temp=self.head
            while temp.next is not self.head:
                temp=temp.next
    
    def delete_at_end(self):
        if self.head is None:
            print("ll is empty")
                       
        else:
            temp=self.head
            while temp.next is not self.head:
                temp=temp.next
            temp.next=self.head 
    
    def delete_at_pos(self, pos):
        if self.head is None:  # Check if the list is empty
            print("The list is empty")
            return

        if pos < 0:  # Check for invalid position
            print("Invalid position")
            return
    
        if pos == 0:  # Delete the head node
            if self.head.next == self.head:  # Only one node in the list
                self.head = None  # Set head to None, list becomes empty
            else:
            # Find the last node to maintain circular link after deletion
                last_node = self.head
                while last_node.next != self.head:  # Traverse to the last node
                    last_node = last_node.next
            
            # Update head and link last node to new head
            self.head = self.head.next
            last_node.next = self.head
        else:  # Delete a node at a specific position
            current = self.head
            count = 0
        
        # Traverse to the node just before the desired position
        while count < pos - 1 and current.next != self.head:
            current = current.next
            count += 1
        
        if count == pos - 1 and current.next != self.head:  # Valid position
            temp = current.next  # Node to be deleted
            current.next = temp.next  # Bypass the node to be deleted
            temp = None  # Free the deleted node
        else:
            print("Position out of range")

obj = CSLL()
obj.insert_at_beg(10)
obj.insert_at_beg(20)
obj.insert_at_beg(30)
obj.insert_at_end(40)
obj.insert_at_pos(25, 2)
print("List after insertions:")
obj.Print()

obj.delete_at_beg()
print("List after deleting the first node:")
obj.Print()

obj.delete_at_end()
print("List after deleting the last node:")
obj.Print()

obj.delete_at_pos(1)
print("List after deleting the node at position 1:")
obj.Print()
