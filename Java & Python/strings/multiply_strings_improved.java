public class Solution {
	public String multiply(String a, String b) {

		ArrayList<Character> res = new ArrayList<>();
		
		int carry = 0, index = 0, num = 0;
		char char_number;

		int index_a = remove_whitespace(a);
		int index_b = remove_whitespace(b);

		if (index_a == -1 || index_b == -1)
			return "0";
		a = a.substring(index_a, a.length());
		b = b.substring(index_b, b.length());

		for (int i = a.length()-1; i >= 0; --i) {
			int _a = a.charAt(i)-'0';
			num = 0;
			int currentIndex = index;

			for (int j = b.length()-1; j >= 0; --j) {
				int _b = b.charAt(j)-'0';
				num = _a*_b + carry;
				carry = num / 10;
				num %= 10;							// make sure num is not double digits
				char_number = (char) (num + '0');

				if (currentIndex >= res.size())
					res.add(char_number);
				else {
					num += res.get(currentIndex)-'0';
					carry += (num/10);
					num %= 10;
					char_number = (char) (num + '0');
					res.set(currentIndex, char_number);
				}
				++currentIndex;
			}
			char_number = (char) (carry + '0');		// in case the carry is not 0, if it's 0 just put 0
			carry = 0;
			res.add(char_number);
			++index;
		}

		Collections.reverse(res);
		int i = remove_whitespace(res);		// starting index w/o 0's
		return convert_to_string(res, i);
	}

	public int remove_whitespace(String a) {
		int i = 0;
		while (i < a.length() && a.charAt(i) == '0')
			++i;
		if (i == a.length())
			return -1;
		return i;
	}
	public int remove_whitespace(ArrayList<Character> res) {
		int i = 0;
		while (i < res.size() && res.get(i) =='0')
			++i;
		return i;
	}
	public String convert_to_string(ArrayList<Character> res, int i) {
		StringBuilder str = new StringBuilder();
		for (; i < res.size(); ++i)
			str.append(res.get(i));
		return str.toString();
	}
}

/*

Given two numbers represented as strings, return multiplication of the numbers as a string.

 Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. 
For example, 
given strings "12", "10", your answer should be “120”.

*/
