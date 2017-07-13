/* Checkpoint */
public class Solution {
    // DO NOT MODIFY THE LIST. IT IS READ ONLY
     public int kthsmallest(final List<Integer> A, int k) {
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        for (int num : A) {
            queue.offer(num);       // insert into queue
            if (queue.size() > k)
                queue.poll();       // removes head of queue
        }
        return queue.peek();
    }
}

/*
Find the kth smallest element in an unsorted array of non-negative integers.

Definition of kth smallest element

 kth smallest element is the minimum possible n such that there are atleast k elements in the array <= n.
In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based ) 
NOTE
You are not allowed to modify the array ( The array is read only ). 
Try to do it using constant extra space.

Example:

A : [2 1 4 3 2]
k : 3

answer : 2
*/