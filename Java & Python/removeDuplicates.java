/**
 * Remove duplicates from sorted array 
 */
public class Solution {
	public int removeDuplicates(ArrayList<Integer> A) {
		int index = 1;
		int length = A.size();

		if (!A || A.size() == 0)	return 0;

		for (int i = 1; i < length; ++i) {
			if (A.get(i).intValue() != A.get(i-1).intValue()) {
				int temp = A.get(index);
				A.set(index, A.get(i));
				++index;
			}
		}
		return index;
	}
}

/*
 1 2 2 3

 index = 1
 i = 1
 	temp = 2
 	A.set(1, A.get(1)) 1, 2, 2, 3
 	index = 2
 i = 2
 	2 = 2
 i = 3
 	temp = 2
 	A.set(2, 3)		1, 2, 3, 3
 	index = 3
 return 3

 .intValue() you have created a list of objects and not Integers 
 get() => Integer, intVaue => int

 */