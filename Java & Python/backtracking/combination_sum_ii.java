public class Solution {
	ArrayList<ArrayList<Integer>> res;
	public ArrayList<ArrayList<Integer>> combinationSum(ArrayList<Integer> A, int target) {
		if (A == null)
			return null;
		res = new ArrayList<>();
		Collections.sort(A);
		helper(A, new ArrayList<>(), target, 0);

		return res;
	}
	public void helper(ArrayList<Integer> A, ArrayList<Integer> arr, int target, int index) {
		if (target == 0) {
			res.add(new ArrayList<>(arr));
			return;
		}
		if (target < 0 || index >= A.size())
			return;
		int i = index + 1;
		for(; i < A.size(); ++i)
			if (A.get(i) != A.get(i-1))
				break;

		helper(A, arr, target, i);
		arr.add(A.get(index));
		helper(A, arr, target - A.get(index), index+1);
		arr.remove(arr.size()-1);
	}
}
/*
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

 Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Example :

Given candidate set 10, 1,2,7,6,1,5 and target 8,

A solution set is:

[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
*/