class Node:
    def __int__(self, data:int):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __int__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')

        return ' -> '.join(nodes)


if __name__ == '__main__':
    linked_list = LinkedList()
    node1 = Node()
    node1.data = 1

    linked_list.head = node1
    node2 = Node()
    node2.data = 2
    node3 = Node()
    node3.data = 3

    node1.next = node2
    node2.next = node3


    print(linked_list)