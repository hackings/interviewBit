/* Subset concept */
public class Solution {
	public ArrayList<ArrayList<Integer>> subsets(ArrayList<Integer> A) {
		Collections.sort(A);
		ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
		for (int a : A) {
			for (ArrayList<Integer> item : res) {
				item.add(a);
				res.add(item);
			}
		}
		return res;
	}
}