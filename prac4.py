# Perform Queues operations using Circular Array implementation.
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Queue:
    def __init__(self, max_size):
        self.head = None
        self.last = None
        self.max_size = max_size
        self.count = 0

    def insert(self, data):
        n_node = Node(data)
        if self.count == self.max_size:
            print("Queue is full")
            return
        if self.head is None:
            self.head = n_node
            self.last = n_node
        else:
            self.last.ref = n_node
            n_node.ref = self.head
            self.last = n_node
        self.count += 1

    def dequeue(self):
        if self.head is None:
            print("No elements in the list. So nothing deleted")
            return
        if self.head == self.last:
            self.head = None
            self.last = None
        else:
            self.head = self.head.ref
        self.count -= 1

    def p_q(self):
        if self.head is None:
            print("Queue is empty")
            return
        node = self.head
        while True:
            print(node.data)
            node = node.ref
            if node == self.head:
                break

a = Queue(4)
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.p_q()
a.insert(5)
print("delete")
a.dequeue()
a.p_q()
