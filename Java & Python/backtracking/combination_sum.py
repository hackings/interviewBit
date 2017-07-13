class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        def aux(res, cur, A, B):
            if sum(cur)>B:
                return
            elif sum(cur)==B:
                if cur not in res:
                    res.append(cur)
                return
            
            for i in A:
                aux(res, sorted(cur+[i]), A, B)
            return
        A.sort()
        res=[]
        aux(res, [], A, B)
        return res
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,
1. Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
2. Entries should be sorted within themselves.

Example :
If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]
"""