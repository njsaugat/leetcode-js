//addition is from right to left; but Linked list is left to right
// so the assumption is the list is in reverse order
class ListNode {
  val;
  next;
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

var addTwoNumbers = function (l1, l2) {
  let sentinel = (tail = new ListNode());

  return addTwoNumbers(l1, l2, tail, sentinel);
};

const add = (l1, l2, tail, sentinel, carry = 0) => {
  const isBaseCase = !(l1 || l2 || carry);

  if (isBaseCase) return sentinel.next;

  return dfs(l1, l2, tail, sentinel, carry);
};

const dfs = (l1, l2, tail, sentinel, carry) => {
  const sum = (l1?.val || 0) + (l2?.val || 0) + carry;

  const val = sum % 10;
  carry = Math.floor(sum / 10);

  tail.next = new ListNode(val);
  tail = tail.next;

  l1 = l1?.next || null;
  l2 = l2?.next || null;

  add(l1, l2, tail, sentinel, carry);

  return sentinel.next;
};

// the easy case is with this while loop

var addTwoNumbers = (l1, l2, carry = 0) => {
  let head = (tail = new ListNode());

  while (l1 || l2 || carry) {
    const sum = (l1?.val || 0) + (l2?.val || 0) + carry;
    const val = sum % 10;
    carry = Math.floor(sum / 10);

    tail.next = new ListNode(val);
    tail = tail.next;

    l1 = l1?.next || null;
    l2 = l2?.next || null;
  }

  return head.next;
};

/**
 * initialize head/tail pointers
 * loop until list next isn't null
 * do calc and move next pointer
 * return head.next since head is empty initailization
 *
 */
