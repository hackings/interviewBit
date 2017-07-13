public class Solution {
	// DO NOT MODIFY THE LIST
	public ArrayList<Integer> searchRange(final List<Integer> a, int b) {
		int left = 0, right = a.size()-1;
		int firstOccurence = -1, secondOccurence = -1;
		int mid = 0;
		ArrayList<Integer> result = new ArrayList<Integer>();
		while (left <= right) {
			mid = (left+right)/2;
			if (a.get(mid) == b) {
				firstOccurence = mid;
				right = mid-1;
			}
			else if (a.get(mid) < b)
				left = mid+1;
			else
				right = mid-1;
		}
		if (firstOccurence == -1) {
			result.add(-1);
			result.add(-1);
			return result;
		}
		left = firstOccurence;
		right = a.size()-1;
		while (left <= right) {
			mid = (left+right)/2;
			if (a.get(mid) == b) {
				secondOccurence = mid;
				left = mid+1;
			} 
			else if (a.get(mid) < b)
				left = mid+1;
			else
				right = mid-1;
		}
		result.add(firstOccurence);
		result.add(secondOccurence);
		return result;
	}
}

/*
	Given a sorted array of integers, find the starting and ending position of a given target value.
	Your algorithm’s runtime complexity must be in the order of O(log n).
	If the target is not found in the array, return [-1, -1].
	Example:
	Given [5, 7, 7, 8, 8, 10]
	and target value 8,
	return [3, 4].

*/
