print("Circular Doubly Linked List")
print('''[[[prev(data3)][data][next(data2)]]-->[[[prev(data1)][data][next(data3)]]-->[[[prev(data2)][data][next(data1)]]]''')

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        newnode = node(data)
        if self.head is None:
            # List is empty; initialize the circular references for the single node
            self.head = newnode
            newnode.next = newnode
            newnode.prev = newnode
        else:
            # List is not empty; insert new node before the current head
            newnode.next = self.head
            newnode.prev = self.head.prev
            self.head.prev.next = newnode
            self.head.prev = newnode
            self.head = newnode
            
    def insert_at_end(self,data):
        newnode=node(data)
        if

    def Print(self):
        # Check if the list is empty
        if self.head is None:
            print("List is empty")
            return

        # Start with the head node
        print("Traversal:")
        print(self.head.data)  # Print the head node's data first

        # Set temp to the second node
        temp = self.head.next

        # Traverse until we loop back to the head
        while temp != self.head:
            print(temp.data)
            temp = temp.next

# Example usage
cdll = CircularDoublyLinkedList()
cdll.insert_at_beginning("data1")
cdll.insert_at_beginning("data2")
cdll.insert_at_beginning("data3")
cdll.Print()
