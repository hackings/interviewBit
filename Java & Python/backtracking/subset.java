/* Need review, just see pythone example */
public class Solution {
    ArrayList<ArrayList<Integer>> res;
    ArrayList<Integer> A;
    int N;
    
	public ArrayList<ArrayList<Integer>> subsets(ArrayList<Integer> A) {
	    ArrayList<Integer> temp;
	    res = new ArrayList<>();
	    temp = new ArrayList<>();
	    this.A = A;
	    N = A.size();
	    Collections.sort(A);
	    subset(0, temp);
	    Collections.sort(res, new Comparator<ArrayList<Integer>>() {
	        @Override
	        public int compare(ArrayList<Integer> a, ArrayList<Integer> b) {
	            for (int i = 0; i < Math.min(a.size(), b.size()); i++) {
	                int cmp = Integer.compare(a.get(i), b.get(i));
	                if (cmp != 0)
	                    return cmp;
	            }
	            return Integer.compare(a.size(), b.size());
	        }
	    });
	    return res;
	}
	
	private void subset(int index, ArrayList<Integer> arr) {
	    if (index == N) {
	        res.add(new ArrayList<>(arr));
	        return;
	    }
	    subset(index + 1, arr);
	    arr.add(A.get(index));
	    subset(index + 1, arr);
	    arr.remove(arr.size() - 1);
	}	
}

/*
arr for [0, 1, 2]
[2][1][1, 2]
[0][0, 2]
[0, 1][0, 1, 2]

A.get(index) 2 1 20212
Given a set of distinct integers, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]
*/