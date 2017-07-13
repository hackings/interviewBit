/* while num is between [0-9], num * 10 + A[i] */
public class Solution {
	public int atoi(final String A) {
		int i = 0, length = A.length();
		long num = 0;
		boolean sign = true;

		while (i < length && A.charAt(i) == ' ')		// get rid of white space
			++i;
		
		if (i == A.length())	
			return 0;	// just have white space
		
		if (A.charAt(i) == '-') {		// negative
			sign = false; 
			++i;
		}
		else if (A.charAt(i) == '+')	// positive
			++i;

		while (i < A.length() && A.charAt(i) >= '0' && A.charAt(i) <= '9') {
			num = Math.abs(num);
			num = num * 10 + (A.charAt(i) - '0');

			if (!sign)
				num = -num;
			if (num > Integer.MAX_VALUE)
				return Integer.MAX_VALUE;
			else if (num < Integer.MIN_VALUE)
				return Integer.MIN_VALUE;
			++i;
		}
		return (int) num;
	}
}

/**
 * Implement atoi to convert a string to an integer.
 * Input : "9 2704"
 * Output : 9
 * 24 ==> 0 * 10 + 2 ==> 2 * 10 + 4 = 24
 * If the number is positive and the current number is greater than MAX_INT/10, and you are about to append a digit, then certainly your number will overflow.
 * If the current number = MAX_INT / 10, then based on the last digit, we can detect if the number will overflow.
 *
 */
