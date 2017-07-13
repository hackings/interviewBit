/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
    	HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
    	RandomListNode root = new RandomListNode(head.label);
    	RandomListNode prev = root;
    	RandomListNode current = head.next;
    	
    	map.put(head, root);

    	while (current != null) {
    		RandomListNode node = new RandomListNode(current.label);	// copy of current
    		map.put(current, node);
    		prev.next = node;

    		current = current.next;
    		prev = prev.next;
    	}
    	current = head;
    	prev = root;
    	while (current != null) {
    		prev.random = map.get(current.random);
    		current = current.next;
    		prev = prev.next;
    	}
    	return root;

    }
}

/*
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or NULL.

Return a deep copy of the list.

Example

Given list

   1 -> 2 -> 3
with random pointers going from

  1 -> 3
  2 -> 1
  3 -> 1
You should return a deep copy of the list. The returned answer should not contain the same node as the original list, but a copy of them. The pointers in the returned list should not link to any node in the original input list.
*/