// However many times you can divide by 5
public class Solution {
	public int trailingZeroes(int a) {
		int num_zeroes = 0;
		while (a/5 > 0) {
			num_zeroes += (a/5);
			a /= 5;
		}
		return num_zeroes;
	}
}

/*
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Example :

n = 5
n! = 120 
Number of trailing zeros = 1
So, return 1
*/
