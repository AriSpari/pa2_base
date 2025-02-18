class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        """
        standard shit
        """
        self.head = None
        self.tail = None
        self.size = 0
        
    
    def push_front(self, data):
        """
        create a new node and make it point to the head, then reassign the head pointer to the new node
        """
        node = Node(data)
        node.next = self.head
        self.head = node
        if size == 0:
            self.tail = node
        self.size += 1
    
    def pop_front(self):
        """
        saves the value of the head node as a variable, reassigns the head to the next node and returns the value of the original head
        """
        ret_val = self.head.value
        self.head = self.head.next
        return ret_val
    
    def push_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        

    def pop_back(self):
        """
        Steppar listann þar til þarnæsta nóða er None, þá vistar það gögnin í næstu nóðu
        og skilgreinir sig sjálfa sem tail
        """
        node = self.head
        if node == None:
            return None
        
        if node.next == None:
            self.tail = None
            self.head = None
            self.size -= 1
            return node.data
        
        while node.next is not None and node.next.next is not None:
            node = node.next
        
        ret_value = node.next.data
        node.next = None
        self.tail = node

        self.size -= 1

        return ret_value

    def get_size(self):
        return self.size

    def __str__(self):
        ret_str = ""
        node = self.head
        while node != None:
            ret_str += str(node.data) + "\n"
            node = node.next
        return ret_str
        
        
        
ari = LinkedList()

print(ari)

ari.push_back(1)
print(ari)
ari.push_back(2)
print(ari)
ari.push_back(3)
ari.push_back(4)
ari.push_back(5)
print(ari)
print("test")
print(ari.pop_back())
print("just popped")
print(ari)
