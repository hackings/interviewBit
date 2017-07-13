/* sum[j] = sum[i-1] */
public class Solution {
    public ArrayList<Integer> lszero(ArrayList<Integer> A) {
    	ArrayList<Integer> res = new ArrayList<Integer>();
    	HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    	if (A == null)
    		return res;
    	int len = 0, sum = 0, l=-1, r = -1;
    	map.put(0, -1);
    	for (int i = 0; i < A.size(); ++i) {
    		sum += A.get(i);
    		if (!map.containsKey(sum))
    			map.put(sum, i);
    		else {
    			if (len < i-map.get(sum)) {
    				l = map.get(sum)+1;
    				r = i;
    				len = i - map.get(sum);
    			}
    		}
    	}
    	if (l >= 0 && r >= 0) {
    		for (int i = l; i <= r; ++i) {
    			res.add(A.get(i));
    		}
    	}
    	return res;
    }
}

/*

Find the largest continuous sequence in a array which sums to zero.

Example:


Input:  {1 ,2 ,-2 ,4 ,-4}
Output: {2 ,-2 ,4 ,-4}

Hint
We need to find j and i such that sum of elements from A[i] to A[j] = 0
 Or Sum[j] - Sum[i-1] = 0
 Or Sum[j] = Sum[i-1]
Now, the problem reduces to finding 2 indices i and j such that sum[i] = sum[j] 
How can you solve the above problem ?
*/