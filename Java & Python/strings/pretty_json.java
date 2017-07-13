/* Doesn't compile - will work on later */

public class Solution {
	public ArrayList<String> prettyJSON(String a) {
		ArrayList<String> res = new ArrayList<String>();
		StringBuilder sb = new StringBuilder();
		int num_tabs = 0;
		char tab = '\t';
		for (int i = 0; i < a.length(); ++i) {
			
			if (a.charAt(i) != ' ')
				sb.append(a.charAt(i));

			if (a.charAt(i) == '{' || a.charAt(i) == '[') {
				if (sb.length() > 2 && sb.charAt(a.length()-2) != tab)
					res.append(sb.substring(0,sb.length()-1));
				sb = tab * num_tabs + a.charAt(i);
				res.append(sb);
				++num_tabs;
			}
			
			else if (a.charAt(i) == '}' || a.charAt(i) == ']') {
				--num_tabs;
				if (sb.length() > 2 && sb.charAt(a.length()-2))
					res.append(sb.substring(0, sb.length()-1));
				sb = tab * num_tabs + a.charAt(i);
			}
			
			else if (a.charAt(i) == ',') {
				res.append(sb);
				sb = tab * num_tabs;
			}
		}
		if (sb.length() > 0 && sb.charAt(sb.length()-1) != tab)
			res.append(sb);

		return res;

	}
}
