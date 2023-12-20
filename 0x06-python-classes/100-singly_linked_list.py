#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        curr_n = self.__head
        if curr_n is None or value < curr_n.data:
            self.__head = Node(value, curr_n)
        else:
            while (curr_n.next_node is not None and
                    value >= curr_n.next_node.data):
                    curr_n = curr_n.next_node
            curr_n.next_node = Node(value, curr_n.next_node)

    def __str__(self):
        string = ""
        if self.__head is not None:
            string = str(self.__head.data)
            curr_n = self.__head.next_node
            while curr_n is not None:
                string += "\n"
                string += str(curr_n.data)
                curr_n = curr_n.next_node
        return string
