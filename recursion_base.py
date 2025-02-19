class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def get_size(head):
    if head == None: # base case
        return 0
    
    if head.next == None: #if head.next is none that means we are at the last node in our list. 
        return 1
    else:
        return 1 + get_size(head.next) # count the node we're at and call the function again with the next node as the argument

def reverse_list(head):
    if head is None or head.next is None:  # Base case: if list is empty or has one node
        return head
    new_head = reverse_list(head.next)  # Reverse the rest of the list
    head.next.next = head  # Make the next node point to the current node
    head.next = None  # Set the current node's next to None
    return new_head 

def palindrome(head):
    """
    creates a new function that takes a pointer to head as an argument. Because it is a pointer it doesn't change with each recursion
    effectively allowing us to maintain a constant pointer to the head node despite moving deeper into the recursive calls. 
    we make the recursive call before the checks so that they are done while returning from the calls (iterating backwards through the list). 
    For each step backwards through the list we compare the element to it's corresponding element at the front and then update the front pointer
    to the next element. if any check returns a False, that false gets sent up the recursive chain and the 'shell' function returns the False. 
    """
     
    def check_palindrome(front_ref, current):
        if current is None: # base case
            return True 

        
        is_pal = check_palindrome(front_ref, current.next)

        if not is_pal: # checks if previous nodes match
            return False

        if front_ref[0].data != current.data: # this is where we compare the node we're at to the correct node at the front of the list
            return False

        front_ref[0] = front_ref[0].next # move the front pointer to the next node

        return True

    return check_palindrome([head], head)  # Pass front node by reference



if __name__ == "__main__":
    ##
    print("GET_SIZE TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = None
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", None)
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", Node("C", None))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)


    ##
    print("REVERSE TESTS")
    print("\n")
    head = Node("A", Node("B", Node("C", Node("D", Node("E", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("A", Node("A", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", None)
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = None
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", None))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)


    ##
    print("PALINDROME TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")
