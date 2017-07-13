public class Solution {
	public int lengthOfLastWord(final String a) {
		String[] tokens = a.split(" +");
		if (tokens.length == 0)
			return 0;
		if (tokens[tokens.length-1] == null || tokens[tokens.length-1].length() == 0)
			return 0;
		return tokens[tokens.length-1].length();
	}
}

/*
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Given s = "Hello World",

return 5 as length("World") = 5.

Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.
*/