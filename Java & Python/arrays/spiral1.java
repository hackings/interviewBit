/* Some small bug */

public class Solution {
	// DO NOT MODIFY THE LIST
	public ArrayList<Integer> spiralOrder(final List<ArrayList<Integer>> a) {
		 ArrayList<Integer> result = new ArrayList<Integer>();

		 int top = 0, bottom = a.size()-1;
		 int left = 0, right = a.get(0).size()-1;

		 int direction = 0;

		 while (top <= bottom && left <= right) {
		 	if (direction == 0) {
		 		for(int i = left; i <= right; ++i)
		 			result.add(a.get(top).get(i));
	 			++top;
	 			direction = 1;
		 	}
		 	else if (direction == 1) {
		 		for (int i = top; i <= bottom; ++i)
		 			result.add(a.get(i).get(right));
		 		--right;
		 		direction = 2;
		 	}
		 	else if (direction == 2) {
		 		for (int i = right; i >= left; --i)
		 			result.add(a.get(bottom).get(i));
		 		--bottom;
		 		direction = 3;
		 	}
		 	else if (direction == 3) {
		 		for (int i = bottom; i >= top; --i)
		 			result.add(a.get(left).get(i));
		 		++left;
		 		direction = 0;
		 	}
		 	else continue;

		 }
		 // Populate result;
		 return result;
	}
}

/* 
Given 
[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

Return
[1, 2, 3, 6, 9, 8, 7, 4, 5]
*/