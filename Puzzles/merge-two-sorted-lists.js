/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    if (!l1) {
        return l2
    }else if (!l2) {
        return l1
    }else if (!l1 && !l2) {
        return []
    }
    let prevNode = new ListNode(Number.NEGATIVE_INFINITY, l1);
    const returnNode = new ListNode(Number.NEGATIVE_INFINITY, l2.val >= l1.val? l1: l2);
    while (l2){
        if (prevNode.val <= l2.val && !l1){
            prevNode.next = l2;
            prevNode = l2;
            l2 = l2.next;
        // If the node should be between prev and current node
        }else if (prevNode.val <= l2.val && l1.val > l2.val) {
            prevNode.next = l2;
            l2 = l2.next;
            prevNode.next.next = l1
            prevNode = prevNode.next;
        }else if (l2.val >= l1.val) {
            prevNode = l1;
            l1 = l1.next;
        }
    }
    return returnNode.next
};