from data_structures.linked_list.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):

        new_node = Node(data)
        new_node.next = self.head

        self.head = new_node

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def search(self, data):

        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next
        return False

    def display(self):

        if self.head is None:
            return

        current = self.head
        values = []
        while current is not None:
            values.append(str(current.data))

            current = current.next

        print("->".join(values))

    def delete(self, data):

        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        previous = self.head
        current = previous.next

        while current is not None:
            if current.data == data:
                previous.next = current.next
                return

            previous = current
            current = current.next

    def length(self):
        length = 0

        current = self.head

        while current is not None:
            length += 1

            current = current.next

        return length

    def insert(self, after, data):

        current = self.head

        while current is not None:
            if current.data == after:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return

            current = current.next
