def mergeLists(head1, head2):
    # Checking if any linkedlist is empty
    if not head1:
        return head2
    elif not head2:
        return head1
    # This is executed if both lists exist
    if head1.data<=head2.data:
        headmerged=head1
        head1=head1.next
    else:
        headmerged=head2
        head2=head2.next
    prevnode=headmerged
    while head1 and head2:
        if head1.data<=head2.data:
            prevnode.next=head1
            head1=head1.next
        else:
            prevnode.next=head2
            head2=head2.next
        prevnode=prevnode.next
    # One of the lists is exhausted
    # The remaining part of the other list is appended at end
    if not head1:
        prevnode.next=head2
    else:
        prevnode.next=head1
    return headmerged

def another_merger(head1, head2):
    dummy = curr = SinglyLinkedListNode(0)
    while head1 and head2:
        if head1.data < head2.data:
            curr.next = head1
            head1, curr = head1.next, head1
        else:
            curr.next = head2
            head2, curr = head2.next, head2

    curr.next = head1 if head1 else head2
    return dummy.next

class SinglyLinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"SinglyLinkedListNode({self.data})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        # find the end of the list.
        node = SinglyLinkedListNode(data)

        if not self.head:
            self.head = node
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = node

    def __repr__(self):
        lst = []
        node = self.head
        while node:
            lst.append(node.data)
            node = node.next
        return f"SinglyLinkedList({lst})"