/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode a, ListNode b) {
        if (a == null)
            return b;
        if (b == null)
            return a;

        ListNode res = new ListNode(0);
        ListNode head = res;
        int carry = 0;

        while (a != null || b != null || carry > 0) {
            int a_val = a == null ? 0 : a.val;
            int b_val = b == null ? 0 : b.val;
            int total = a_val + b_val + carry;
            int val = total % 10;
            res.next = new ListNode(val);
            res = res.next;
            carry = total / 10;            
            if (a != null)
                a = a.next;
            if (b != null)
                b = b.next;
        }
        return head.next;
    }
}

/*


You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

3 1 + 9

item to put in linked list 12 % 10 = 2
carry = 12 / 10

13 + 9 = 2


899
238
  7

carry starts out as 0
8 + 9 = 17
17 % 10 = 7
carry 17 / 10 = 1

(9 +  3 + carry)%10 = item 
*/