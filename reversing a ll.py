# Definition for a singly linked list node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definition for singly linked list
class SLL:
    def __init__(self):
        self.head = None

# Function to reverse the linked list in-place
def reversell(head):
    prev = None
    current = head  # Changed from Self.head to head

    while current is not None:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to current
        current = next_node       # Move current to next_node

    # After the loop, prev will be the new head
    return prev

# Utility function to print the linked list
def print_list(head):
    current = head  # Changed from heead.head to head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example Usage:
# Create the linked list 1 -> 2 -> 3 -> 4 -> None
head = Node(1)                  # Changed heead to head
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original Linked List:")
print_list(head)

# Reverse the linked list
reversed_head = reversell(head)

print("Reversed Linked List:")
print_list(reversed_head)
