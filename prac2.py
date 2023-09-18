# operation on linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def search(self, target):
        temp = self.head
        index = 1
        while temp:
            if temp.data == target:
                print(f"{target} is found at index: {index}")
                return
            temp = temp.next
            index += 1
        print(f"{target} is not found in the list.")

    def printlist(self):
        temp = self.head
        if not temp:
            print("The list is empty.")
            return
        print("The list contains:", end="")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage:
my_linked_list = LinkedList()
my_linked_list.push_back(10)
my_linked_list.push_back(20)
my_linked_list.push_back(30)

my_linked_list.printlist()
my_linked_list.search(10)
my_linked_list.search(15)
my_linked_list.search(20)