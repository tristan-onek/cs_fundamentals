# Major data structures demo
# Written by Tristan Onek

# 1. Lists:
print("1. List (Dynamic array)")
my_list = [1, 2, 3, 4]
# Adding an element to the list
my_list.append(5)
# Lists are mutable and maintain order
print("After append:", my_list)  # Output: [1, 2, 3, 4, 5]

# 2. Tuples:
print("\n2. Tuple (Immutable array)")
my_tuple = (1, 2, 3, 4)
# Accessing an element
print("Element at index 2:", my_tuple[2])  # Output: 3
# Tuples are immutable; you can't modify them

# 3. Sets:
print("\n3. Set (Unordered collection of unique elements)")
my_set = {1, 2, 2, 3, 4}
# Adding an element
my_set.add(5)
print("After adding 5:", my_set)  # Output: {1, 2, 3, 4, 5}

# 4. Dictionary (KVPs):
print("\n4. Dictionary (Key value pairs)")
my_dict = {"a": 1, "b": 2, "c": 3}
# Adding a new key-value pair
my_dict["d"] = 4
print("...After adding ('d': 4):", my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 5. Stack:
print("\n5. Stack (e.g. LIFO)")
stack = []
# Pushing elements onto the stack...
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after pushing:", stack)  # Output: [1, 2, 3]
# Popping an element
print("Popped element:", stack.pop())  # Output: 3
print("Stack after popping:", stack)  # Output: [1, 2]

# 6. Queue:
print("\n6. Queue (FIFO)")
from collections import deque
queue = deque()
# Queue elements
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueues:", queue)  # Output: deque([1, 2, 3])
# Dequeue an element
print("Dequeued element:", queue.popleft())  # Output: 1
print("After dequeue:", queue)  # Output: deque([2, 3])

# 7. Priority Queue:
print("\n7. Priority Queue (heapq)")
import heapq
priority_queue = []
# Adding elements
heapq.heappush(priority_queue, 3)
heapq.heappush(priority_queue, 1)
heapq.heappush(priority_queue, 2)
print("Priority queue after pushes:", priority_queue)  # Output: [1, 3, 2]
# Popping the smallest element
print("Popped smallest element:", heapq.heappop(priority_queue))  # Output: 1
print("Priority queue after pop:", priority_queue)  # Output: [2, 3]

# 8. Linked List:
print("\n8. Linked List")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
print("Linked list:")
linked_list.print_list()  # Output: 1 -> 2 -> 3 -> None

# 9. Graph Adjacency list demo:
print("\n9. Graph (Adjacency list)")
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

print("Graph adjacency list:", graph)
# Access neighbors of a node
print("Neighbors of node 2:", graph[2])  # Output: [0, 3]

# 10. Binary Tree:
print("\n10. Binary Tree")
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert_left(self, current_node, value):
        current_node.left = TreeNode(value)

    def insert_right(self, current_node, value):
        current_node.right = TreeNode(value)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

tree = BinaryTree(1)
tree.insert_left(tree.root, 2)
tree.insert_right(tree.root, 3)
print("In-order traversal of tree:")
tree.inorder_traversal(tree.root)  # Output: 2 1 3
print()
