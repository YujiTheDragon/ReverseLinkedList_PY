
class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None


def list_length(first_node):
    assert first_node is not None

    count = 0
    curr = first_node

    while curr.next is not None:
        count += 1
        curr = curr.next

    return count


def list_add(first_node, val):
    assert first_node is not None

    curr = first_node

    while curr.next is not None:
        curr = curr.next

    curr.next = Node(val)


def print_list(first_node):
    assert first_node is not None
    curr = first_node

    while curr:
        print(curr.value)
        curr = curr.next

def reverse_list(first_node):
    assert first_node is not None
    curr = first_node
    next = None
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev
        

my_first_node = Node(0)
list_add(my_first_node, 1)
list_add(my_first_node, 5)
list_add(my_first_node, 8)

#print_list(my_first_node)
print_list(reverse_list(my_first_node))