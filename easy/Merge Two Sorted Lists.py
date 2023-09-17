# Definition for singly-linked list.
# Merging two sorted list nodes
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # init listNode
    head = ListNode()
    # set current pointer to head
    current = head
    # while one of the lists doesn't point to none enter while
    while list1 and list2:
        # check to see bigger int(VALUE) in list
        if list1.val > list2.val:
            # point the next head to the current head of list 2
            current.next = list2
            # list2 fast-forward to next pointer
            list2 = list2.next
        # list1 has the smaller number
        else:
            # point the next head to the current of list 1
            current.next = list1
            # list1 next head pointer will be its next
            list1 = list1.next
        # lastly we move the head on position forward and get ready to enter next value expected
        current = current.next
    # one list has ended and has None as its .next pos,
    # so we append the rest of the list that has still values in it to our next head
    current.next = list1 or list2
    # head hasn't moved only current did, and we slice the node from the heads second pos
    return head.next
