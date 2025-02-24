class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():#mér sýnist allt saman virka
    def __init__(self):
        """
        standard shit
        """
        self.head = None
        self.tail = None
        self.size = 0
        
    
    def push_front(self, data):#virkar
        """
        create a new node and make it point to the head, then reassign the head pointer to the new node
        """
        node = Node(data)
        node.next = self.head
        self.head = node
        if self.size == 0:
            self.tail = node
        self.size += 1
    
    def pop_front(self):#virkar
        """
        saves the value of the head node as a variable, reassigns the head to the next node and returns the value of the original head
        """
        if self.head == None:
            return
        ret_val = self.head.data
        self.head = self.head.next
        self.size -= 1
        return ret_val
    
    def push_back(self, data):#virkar
        """
        creates a new node. if it's the first node to be creaated then it is both the head and the tail, otherwise it is just the tail. also links the old tail to this new one.
        """
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        

    def pop_back(self): #virkar
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

    def get_size(self):#virkar
        """
        The class keeps track of the size of the list so we simply return that value. 
        """
        return self.size

    def __str__(self):#virkar
        """
        recursively builds a string from the data in the nodes and strips the trailing space. 
        """
        ret_str = ""
        node = self.head
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str.strip()
        
        