'''

LeetCode LinkedList Q.876 Middle of the Linked List
Recusion and Slow/Fast Pointer Solution

'''


def middleNode(self, head: ListNode) -> ListNode:

    def rec(slow, fast):
        if not fast:
            return slow
        elif not fast.next:
            return slow
        return rec(slow.next, fast.next.next)

    return rec(head, head)
