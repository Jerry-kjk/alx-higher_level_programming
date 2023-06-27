#!/usr/bin/python3

"""Define a node of a singly linked list."""


class Node:
     """Represent a node in a singly-linked list."""

     def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
        elif value < self.head.data:
            # If the value is smaller than the head's data,
            # insert the new node at the beginning of the list
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                # Traverse the list to find the correct position for insertion
                current = current.next_node

            # Insert the new node between current and current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        output = ""
        current = self.head

        while current is not None:
            # Traverse the list and concatenate the data of each node
            output += str(current.data) + "\n"
            current = current.next_node

        return output.strip()
