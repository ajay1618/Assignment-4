#Implement deletion operation from the end of the linked list and Insertion operation from the beginning of the linked list

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, position):

        if self.head == None:
            return

        temp_node = self.head

        if position == 0:
            self.head = temp_node.next
            temp_node = None
            return

    def printList(self):
        temp_node = self.head
        while (temp_node):
            print(str(temp_node.item) + " ", end="")
            temp_node = temp_node.next


if __name__ == '__main__':

    llist = LinkedList()


    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAtBeginning(8)
    llist.insertAtBeginning(6)
    llist.insertAtBeginning(5)

    print('Linked list:')
    llist.printList()
    print("after inserting at the beginning :")
    llist.insertAtBeginning(10)
    llist.printList()
    print("\nAfter deleting an element:")
    llist.deleteNode(0)
    llist.printList()
