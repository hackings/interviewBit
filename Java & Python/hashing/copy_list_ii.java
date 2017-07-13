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
    	HashMap<RandomListNode, RandomListNode> map = new HashMap<>();
    	RandomListNode current = head;
    	RandomListNode newNode;
    	RandomListNode newHead = null;

    	while (current != null) {
    		newNode = new RandomListNode(current.label);
    		if (newHead == null)
    			newHead = newNode;
    		map.put(current, newNode);
    		current = current.next;
    	}
    	for (Map.Entry<RandomListNode, RandomListNode> entry : map.entrySet()) {
    		RandomListNode node = entry.getKey();
    		newNode = entry.getValue();
    		if (node.next != null)
    			newNode.next = map.get(node.next);
    		if (node.random != null)
    			newNode.random = map.get(node.random);
    	}
    	return newHead;
    }
}