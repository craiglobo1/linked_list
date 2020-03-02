class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = Node()
    def append(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        return elems
    def prepend(self,data):
        new_node = Node()
        self.append(None)
        cur = self.head
        nextData = 0
        while cur.next != None:
            cur = cur.next
            cur.data = nextData
            nextData = cur.data
        
            


if __name__ == '__main__':
    listLink = LinkedList()
    print(listLink.display())
    listLink.append(2)
    print(listLink.display())
    listLink.prepend(5)
    print(listLink.display())
    listLink.append(8)
    print(listLink.display())

