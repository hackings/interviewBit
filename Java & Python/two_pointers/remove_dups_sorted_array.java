public class Solution {
	public int removeDuplicates(ArrayList<Integer> a) {
		int length = a.size();
		int index = 1;
		if (length == 0 || length == 1)
			return length;

		for (int i = 1; i < a.size(); ++i) {
			if (a.get(i).intValue() != a.get(i-1).intValue()) {
				int temp = a.get(index);
				a.set(index, a.get(i));
				++index;
			}
		}
		return index;
	}
}
/*
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

 Example: 
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].*/