/* leftRemaining, rightRemaining, make str[2*count]
str[count] = '(' then do recursion
*/

public class Solution {
	void addParen(ArrayList<String> res, int leftRem, int rightRem, char[] str, int count) {
	if (leftRem < 0 || rightRem < leftRem)
		return;
	if (leftRem == 0 && rightRem == 0) {
		String s = String.copyValueOf(str);
		res.add(s);
	}
	else {
		if (leftRem > 0) {
			str[count] = '(';
			addParen(res, leftRem-1, rightRem, str, count+1);
		}
		if (rightRem > leftRem) {
			str[count] = ')';
			addParen(res, leftRem, rightRem-1, str, count+1);
		}
	}
}
	ArrayList<String> generateParenthesis(int count) {
		char[] str = new char[count*2];
		ArrayList<String> res = new ArrayList<>();
		addParen(res, count, count, str, 0);
		return res;
	}
}

/*
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
Make sure the returned list of strings are sorted.

add(list, 3, 3, str, 0)
	s = (
	addParen(2, 3, str, 1)
		s = ((
		addParen(1, 3, str, 2)
		s = (((
			addParen(0, 3, str, 3)
			s = ((()
				addParen(0, 2, str, 4)
				s = ((())
					addParen(0, 1, str, 5)
					s = ((()))
						addParen(0, 0, str, 6)
		s = (()())
	s = (())()
s = ()(())
*/