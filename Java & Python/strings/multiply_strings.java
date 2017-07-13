/* This solution doesn't take into account integer overflow */
public class Solution {
	public String multiply(String a, String b) {
		if (a == null || b == null)
			return null;
		int num = stringToNum(a)*stringToNum(b);
		return Integer.toString(num);
		//return numToString(num);
	}
	public int stringToNum(String s) {
		int i = 0;
		int num = 0;
		while(i < s.length() && s.charAt(i) >= '0' && s.charAt(i) <= '9'){
			num = 10 * num + (s.charAt(i)-'0');
			++i;
		}
		return (int) num;
	}
	public String numToString(int num) {
		StringBuilder sb = new StringBuilder();
		int current;
		while (num > 0) {
			current = num % 10;
			sb.insert(0, current);
			num /= 10;
		}
		return sb.toString();
	}
}

/*

Given two numbers represented as strings, return multiplication of the numbers as a string.

 Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. 
For example, 
given strings "12", "10", your answer should be “120”.
*/