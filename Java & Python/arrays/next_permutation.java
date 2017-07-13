public class Solution {
	public void nextPermutation(ArrayList<Integer> A) {
		boolean status;
		status = nextPerm(A);
		if (!status)
			Collections.sort(A);
		return;
	}

	public boolean nextPerm(ArrayList<Integer> A) {
		int i = 0; 
		int n = A.size();

		for (i = n-2; i >= 0; --i) 
			if (A.get(i) < A.get(i+1))
				break;
		
		if (i == -1)	return false;

		int j = n-1;
		for(; j >= i; --j) 
			if (A.get(j) > A.get(i))
				break;

		swap (A, i, j);
		++i;

		int steps = (n-i+1)/2;
		for (int k = 0; k < steps; ++k)
			swap(A, i+k, n-k-1);

		return true;
	}

	public void swap(ArrayList<Integer> A, int i, int j) {
		int temp = A.get(i);
		A.set(i, A.get(j));
		A.set(j, temp);
	}
}

/*
	 1, 2, 3, 4, 5
	---------------
	i = 3, j = 4
	4 >= 3

	1, 2, 3, 5, 4
	i = 4
	steps = (5-4+1)/2 = 1
	k = 0
	swap(4, 5-0-1)
 */