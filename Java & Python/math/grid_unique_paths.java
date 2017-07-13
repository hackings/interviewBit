public class Solution {
	public int uniquePaths(int m, int n) {
		// (m + n - 2) C (n-1) = (m+n-2)! / (n-1)! (m-1)! 
		// Combination order is not important
		// C(n, r) = n! / (r! (n-r)!)
		double ways = 1;
		for (int i = n; i < m + n - 1; ++i) {
			ways *= i;
			ways /= (i - n + 1);
		}
		return (int)ways;
	}
}

/*
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :

Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
              OR  : (0, 0) -> (1, 0) -> (1, 1)
*/