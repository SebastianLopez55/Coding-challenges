from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        # Use fast and slow pointers to find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHalfHead = slow.next
        prev = slow.next = None
        # Reverse the second half of LList
        while secondHalfHead:
            tmp = secondHalfHead.next
            secondHalfHead.next = prev
            prev = secondHalfHead
            secondHalfHead = tmp

            # Merge two halfs
        firstHalfHead, secondHalfHead = head, prev
        while secondHalfHead:
            tmp1, tmp2 = firstHalfHead.next, secondHalfHead.next
            firstHalfHead.next = secondHalfHead
            secondHalfHead.next = tmp1
            firstHalfHead, secondHalfHead = tmp1, tmp2



# create the linked list
head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4


# create an instance of the Solution class and call the function with the linked list
solution = Solution()

node = head
# Input LList:
print("Input LList")
arr = []
while node:
    link = (f" {node.val} > ")
    arr.append(link)
    node = node.next
print(arr)

solution.reorderList(head)

# print the values in the modified linked list to verify that the function worked correctly
node = head
# Input LList:
print("Output LList")
arr = []
while node:
    link = (f" {node.val} > ")
    arr.append(link)
    node = node.next
print(arr)
