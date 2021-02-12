# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
        [
        1->4->5,
        1->3->4,
        2->6
        ]
    merging them into one sorted list:
        1->1->2->3->4->4->5->6

Example 2:

    Input: lists = []
    Output: []

Example 3:

    Input: lists = [[]]
    Output: []

Constraints:

    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] is sorted in ascending order.
    The sum of lists[i].length won't exceed 10^4.

https://leetcode.com/problems/merge-k-sorted-lists/
"""
class Solution:
    """
        Loop while we lists is not empty.
        Check which node of the linked lists is least and set it as 
        the next node and set that node equal to it's next. 
        if a list is empty remove it from lists.
        
        For every Linked List in lists. Loop through nodes till you reach the end,
        appending each node to nodes. Sort nodes. Add every node in nodes together and return output.next
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        
        for node in lists:
            while node:
                nodes.append(node.val)
                node = node.next
                
        nodes.sort()
        
        output = ListNode()
        curNode = output
        
        for val in nodes:
            curNode.next = ListNode(val)
            curNode = curNode.next
            
        return output.next