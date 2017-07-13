public class Solution {
	public ArrayList<ArrayList<Integer>> permute(ArrayList<Integer> a) {
		ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
		res.add(new ArrayList<Integer>());

		for (int i = 0; i < a.size(); ++i) {
			Set<ArrayList<Integer>> currentSet = new HashSet<ArrayList<Integer>>();
			for (List<Integer> l : res) {
				for (int j = 0; j < l.size()+1; ++j) {
					l.add(j, a.get(i));
					ArrayList<Integer> T = new ArrayList<Integer>(l);
					l.remove(j);

					currentSet.add(T);
				}
			}

			res = new ArrayList<ArrayList<Integer>>(currentSet);
		}
		return res;
	}
}
/*

All Unique Permutations

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example :
[1,1,2] have the following unique permutations:

[1,1,2]
[1,2,1]
[2,1,1]
 NOTE : No 2 entries in the permutation sequence should be the same. 
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS. Example : next_permutations in C++ / itertools.permutations in python.
If you do, we will disqualify your submission retroactively and give you penalty points. *
