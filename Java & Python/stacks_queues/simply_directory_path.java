/* Concept but doesn't work out correctly due to stack to array to string */
public class Solution {
    public String simplifyPath(String url) {
        String[] parts = url.split("/+");
        String[] res;
        Stack<String> s = new Stack<String>();
        for (String item : parts) {
            if (item == "..")
                if (s.size() > 0)
                    s.pop();
            else if (item == ".")
                continue;
            else if (item.length() != 0)
                s.push(item);
            
        }
        res = s.toArray(new String[parts.length]); // issue here
        String result = String.join("/", res);
        return result;
    }  
}


/*

Given an absolute path for a file (Unix-style), simplify it.

Examples:

path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Note that absolute path always begin with ‘/’ ( root directory )
Path will not have whitespace characters.
*/