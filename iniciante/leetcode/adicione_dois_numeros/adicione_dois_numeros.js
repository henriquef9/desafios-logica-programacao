
// Definition for singly-linked list.

function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    

};


let l1 = new ListNode(2, new ListNode(4, new ListNode(3)));

// Criando l2: 5 -> 6 -> 4
let l2 = new ListNode(5, new ListNode(6, new ListNode(4)));

let result = addTwoNumbers(l1, l2);

// Mostrar resultado:
while (result) {
    console.log(result.val);  
    result = result.next;
}