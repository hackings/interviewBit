public class Solution {
	public String fractionToDecimal(int numerator, int denominator) {
		long a = numerator, b = denominator;
		if (a%b == 0)	
			return String.valueOf(a/b);
		HashMap<Long,Integer> map = new HashMap<Long, Integer>();
		StringBuilder sb = new StringBuilder();
		if ((numerator < 0)^(denominator < 0))
			sb.append("-");
		a = Math.abs(a);
		b = Math.abs(b);

		sb.append(a/b+".");
		long remainder = (a % b) * 10;
		
		while (!map.containsKey(remainder)) {
			if (!map.containsKey(remainder)) {
				map.put(remainder, sb.length());
				sb.append(String.valueOf(remainder/b));
				remainder = (remainder % b)*10;

				if (remainder == 0)
					return sb.toString();
			}
		}
		sb.insert(map.get(remainder), "(");
		sb.append(")");
		return sb.toString();

	}
}



/*
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example :

Given numerator = 1, denominator = 2, return "0.5"
Given numerator = 2, denominator = 1, return "2"
Given numerator = 2, denominator = 3, return "0.(6)

1) multiply the remainder by 10, 
2) append remainder / denominator to your decimals
3) remainder = remainder % denominator.
At any moment, if your remainder becomes 0, you are done.
If you start with remainder = R at any point with denominator d, you will always get the same sequence of digits. 
So, if your remainder repeats at any point of time, you know that the digits between the last occurrence of R will keep repeating.
*/