public class Solution {
	public ArrayList<ArrayList<Integer>> diagonal(ArrayList<ArrayList<Integer>> A) {
		int n = A.size();
		ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>();
		for (int i = 0; i < 2*n-1; ++i) {
			int offset = i < n ? 0 : i-n+1;
			ArratList<Integer> row = new ArrayList<Integer>();
			for (int j = offset; j <= i - offset; ++j) 
				row.add(A.get(j).get(i-j));
			
			res.add(row);
		}
		return res;
	}
}
/*
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:

		
Input: 	

1 2 3
4 5 6
7 8 9

Return the following :

[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


Input : 
1 2
3 4

Return the following  : 

[
  [1],
  [2, 3],
  [4]
]*/
