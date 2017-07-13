/* 70/8 != 8, but closest thing is 8
 add extra variable if (mid <= a/mid) root = mid, low = mid+1
*/

public class Solution {
	public int sqrt(int a) {
		int low = 1;
		int high = a;
		int root = 0;
		int mid;

		while (low <= high) {
			mid = (low+high)/2;

			if (mid == a/mid)
				return mid;
			if ( mid <= a/mid) {
				root = mid;		// if it's not perfect, return floor
				low = mid +1;	
			}
			else
				high = mid-1;
		}
		return root;
	}
}


/*
Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

Input : 11
Output : 3 
*/