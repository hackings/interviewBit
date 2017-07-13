public class Solution {
    ArrayList<ArrayList<Integer>> res;
    public ArrayList<ArrayList<Integer>> subsetsWithDup(ArrayList<Integer> A) {    
        res = new ArrayList<>();            
        if (A == null)
            return null;
        Collections.sort(A);
        subset(A, new ArrayList<>(), 0);
        Collections.sort(res, new Comparator<List<Integer>> () {
            @Override
            public int compare(List<Integer> a, List<Integer> b) {
                int size = Math.min(a.size(), b.size());
                for (int i = 0; i < size; i++) {
                    int cmp = Integer.compare(a.get(i), b.get(i));
                    if (cmp != 0)
                        return cmp;
                }
                return Integer.compare(a.size(), b.size());
            }
        });
        return res;
    }
    
    public void subset(ArrayList<Integer> A, ArrayList<Integer> arr, int index) {
        if (index >= A.size()) {
            res.add(new ArrayList<>(arr));
            return;
        }
        int curIndex = index + 1;
        while (curIndex < A.size() && A.get(curIndex) == A.get(index))
            curIndex++;
        for (int i = 0; i <= (curIndex - index); i++) {
            for (int j = 0; j < i; j++)
                arr.add(A.get(index));
            subset(A, arr, curIndex);     //
            for (int j = 0; j < i; j++)
                arr.remove(arr.size() - 1);
        }
    }
}

/*
Given a collection of integers that might contain duplicates, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
Example :
If S = [0,2,2], the solution is:

[
[],
[0],
[0,2],
[0,2,2],
[2],
[2, 2]
]
*/