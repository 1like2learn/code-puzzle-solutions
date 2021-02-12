/**
 * 
 * Given a linked list, swap every two adjacent nodes and return its head.
 * 
Example 1:

    Input: head = [1,2,3,4]
    Output: [2,1,4,3]

Example 2:

    Input: head = []
    Output: []

Example 3:

    Input: head = [1]
    Output: [1]

Constraints:

    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100

 
Follow up: Can you solve the problem without modifying the values in the list's nodes? (i.e., Only nodes themselves may be changed.)
https://leetcode.com/problems/swap-nodes-in-pairs/
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
/**
* Zero represents the previous node. One and Two represent the current nodes we are swapping.
* We run the loop while Two is truthy. Make Zero.next Two, swap One and Two. Set up the loop for the next run.
*/
let swapPairs = function(head) {
    const resultNode = new ListNode(0)
    let node0 = resultNode;
    let node1 = head;
    let node2 = head?.next;
    
    if (!node2) {
        return head
    }
    
    while (node2) {
        
        // Swap nodes
        node0.next = node2;
        node1.next = node2?.next;
        node2.next = node1
        
        // Setup next loop
        node0 = node1
        node1 = node1?.next
        node2 = node1?.next
        
    }
    
    return resultNode.next;
};