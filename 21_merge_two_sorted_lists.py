# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))


def mergeTwoLists(list1, list2):

    cur = dummy = ListNode()

    while list1 and list2:

        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2

    if list1 or list2:
        cur.next = list1 if list1 else list2

    return dummy.next


def merge(s, t):

    if not s:
        return t
    elif not t:
        return s
    elif s.val <= t.val:
        return ListNode(s.val, merge(s.next, t))
    else:
        return ListNode(t.val, merge(s, t.next))


def merge_in_place(s, t):

    if s is None:       #s.val is none
        return t
    elif t is None:     #t.val is none
        return s
    elif s.val <= t.val:
        s.next = merge_in_place(s.next, t)
        return s
    else:
        t.next = merge_in_place(s, t.next)
        return t

merge_in_place(list1, list2)
