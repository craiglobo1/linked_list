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
        cur = self.head.next
        nextData = 0
        while cur.next != None:
            newData =cur.data
            cur = cur.next
            cur.data = newData
        self.head.next.data = data
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            cur = cur.next
            total += 1
        return total
    def get(self,index):
        cur_idx = 0
        cur =self.head
        if index > self.length():
            return 'Error: out of index'
        while index > cur_idx-1:
            cur = cur.next
            cur_idx += 1
        return cur.data
    def remove(self,index):
        cur_idx = 0
        cur =self.head
        if index > self.length():
            return 'Error: out of index'
        while index > cur_idx:
            cur = cur.next
            cur_idx += 1
        cur.next =cur.next.next
            
            

if __name__ == '__main__':
    listLink = LinkedList()
    print(listLink.display())
    listLink.append(2)
    print(listLink.display())
    listLink.prepend(5)
    print(listLink.display())
    listLink.append(8)
    print(listLink.display())
    print(f'The length is: {listLink.length()}')
    print(listLink.get(0))
    listLink.remove(1)
    

