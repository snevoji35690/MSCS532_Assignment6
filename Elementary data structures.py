# 1. Array
class Array:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        return None

a = Array()
a.insert(10)
a.insert(20)
a.delete(0)
print("Array:", a.data)
print("Access index 0:", a.access(0))


# 2. Matrix
class Matrix:
    def __init__(self, rows, cols):
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def insert(self, row, col, value):
        self.data[row][col] = value

    def delete(self, row, col):
        self.data[row][col] = 0

    def access(self, row, col):
        return self.data[row][col]

m = Matrix(2, 2)
m.insert(0, 1, 5)
m.insert(1, 0, 9)
print("Matrix:", m.data)
print("Access (1, 0):", m.access(1, 0))


# 3. Stack
class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop() if self.data else None

    def peek(self):
        return self.data[-1] if self.data else None

    def is_empty(self):
        return len(self.data) == 0

s = Stack()
s.push(1)
s.push(2)
print("Stack peek:", s.peek())
print("Stack pop:", s.pop())


# 4. Queue
class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0) if self.data else None

    def peek(self):
        return self.data[0] if self.data else None

    def is_empty(self):
        return len(self.data) == 0

q = Queue()
q.enqueue(100)
q.enqueue(200)
print("Queue dequeue:", q.dequeue())
print("Queue peek:", q.peek())


# 5. Singly Linked List
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    def traverse(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

ll = SinglyLinkedList()
ll.insert(3)
ll.insert(5)
ll.insert(7)
ll.delete(5)
print("Linked List Traverse:", ll.traverse())


# 6. Tree (Optional)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def traverse(self):
        result = [self.value]
        for child in self.children:
            result.extend(child.traverse())
        return result

root = TreeNode("A")
child1 = TreeNode("B")
child2 = TreeNode("C")
root.add_child(child1)
root.add_child(child2)
child1.add_child(TreeNode("D"))
print("Tree Traverse:", root.traverse())
