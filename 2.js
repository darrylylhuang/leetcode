// 2. Add Two Numbers

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
var addTwoNumbers = function (l1, l2) {
  return addTwoNumbersHelper(l1, l2);
};

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @param {number} carry
 * @return {ListNode}
 */
var addTwoNumbersHelper = function (l1, l2, carry = 0) {
  let val = 0;

  if (l1 === null && l2 === null && carry === 0) return null;
  if (l1 !== null) {
    next1 = l1.next;
    val += l1.val;
  }
  if (l2 !== null) {
    next2 = l2.next;
    val += l2.val;
  }

  val += carry;

  let nextCarry = 0;
  if (val > 9) nextCarry++;
  return new ListNode(val % 10, addTwoNumbersHelper(next1, next2, nextCarry));
};

class ListNode {
  constructor(val, next) {
    if (Array.isArray(val)) {
      this.val = val[0];
      this.next = val.length === 1 ? null : new ListNode(val.slice(1));
    } else {
      this.val = val === undefined ? 0 : val;
      this.next = next === undefined ? null : next;
    }
  }
}

var testCases = function () {
  // l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
  // l2 = new ListNode(5, new ListNode(6, new ListNode(4)));
  // test(l1, l2);

  // l1 = new ListNode([0]);
  // l2 = new ListNode([0]);
  // test(l1, l2);

  l1 = new ListNode([9, 9, 9, 9, 9, 9, 9]);
  l2 = new ListNode([9, 9, 9, 9]);
  test(l1, l2);
};

var test = function (l1, l2) {
  console.log(`l1 = ${l1}`);
  console.log(`l2 = ${l2}`);
  let sum = addTwoNumbers(l1, l2);
  console.log("Sum:");
  while (sum !== null) {
    console.log(sum);
    sum = sum.next;
  }
};

testCases();
