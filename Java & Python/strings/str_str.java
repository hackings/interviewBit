public class Solution {
    public int strStr(final String haystack, final String needle) {
    	if (haystack.length() == 0 || needle.length() == 0)
	        return -1;
	    if (needle.length() > haystack.length())
	        return -1;
	    boolean isMatched = true;

	    for (int i = 0; i < haystack.length(); ++i) {
			isMatched = true;
	    	for (int j = 0; j < needle.length(); ++j) {
	    		if (i+j > haystack.length()-1) 
	    			return -1;
	    		if (haystack.charAt(i+j) != needle.charAt(j)) {
	    			isMatched = false;
	    			break;
	    		}
	    	}
	    	if (isMatched)
	    		return i;
	    }
	    return -1;
	}
}
	    