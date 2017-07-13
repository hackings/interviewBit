/* Num array, roman numeral array, subbtract total from greatest A first, then append corresponding val */
public class Solution {
	public String intToRoman(int n) {
	    int[] A = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
	    String[] B = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
	    StringBuilder sb = new StringBuilder();
	    for(int i=0; i<A.length; i++) {
	        while(n >= A[i]) {
	            sb.append(B[i]);
	            n -= A[i];
	        }
	    }
	    return sb.toString();
	}
}