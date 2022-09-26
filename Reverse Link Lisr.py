class node:
    def __init__(self, value):
        self.next = None
        self.value = value

a = node(1)
b = node(2)
c = node(3)
d = node(4)

a.next = b
b.next = c
c.next = d


def print_link(head):
    if head is None :
        print("None" )
        return

    print(head.value , end=" -> ")
    print_link(head.next)


def rev_link(head):
    if head is None :return head
    if head.next is None : return head

    new_node = rev_link(head.next)
    head.next.next = head
    head.next = None

    return new_node

print_link(a)
new = rev_link(a)
print_link(new)