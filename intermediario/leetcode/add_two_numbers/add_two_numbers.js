
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
    let result = new ListNode(0, undefined);

    let l = l1;
    let r = l2;
    let current = result;

    let sobra = 0; 

    while(l != null || r != null ){

        let soma = current.val;

        if(l != null){
            soma += l.val; 
            l = l.next;    
        }
        
        if(r != null){
            soma += r.val;
            r = r.next;    
        }

        current.val = soma % 10;
        sobra = parseInt(soma / 10);

        if(!(r == null && l == null && sobra == 0)){
            current.next = new ListNode(sobra, undefined); 
            current = current.next;
        }
        

    }

    return result;

};

// teste

let l1 = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9)))))));

let l2 = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9))));

// let l1 = new ListNode(2, new ListNode(4, new ListNode(3)));

// let l2 = new ListNode(5, new ListNode(6, new ListNode(4)));


let result = addTwoNumbers(l1, l2);

while (result) {
    console.log(result.val);  
    result = result.next;
}