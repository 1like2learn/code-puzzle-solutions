"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # cache all the nodes in the Linked List
        # i will be the key for the last node in the list
        cache = {}
        i = 0
        while head:
            cache[i] = head
            i += 1
            head = head.next
        
        # first case is for when the node to remove is not at the beggining or the end
        if i - n > 0 and n != 1:
            node = cache[i - n - 1]
            node.next = cache[i - n + 1]
            return cache[0]
        # second case is for when the node to remove is at the end
        elif i - n > 0:
            cache[i - n - 1].next = None
            return cache[0]
        # third case is for when the node to remove is at the beginning
        elif n != 1:
            return cache[1]
        # fourth case is for when the node to remove is the only node in the list
        else:
            return None