class Solution:
	# @param A : list of strings
	# @return a list of strings
	def prefix(self, A):
		tree = [0, dict()]
		for s in A:
			node = tree
			node[0] += 1
			for c in s:
				node = node[1].setdefault(c, [0, dict()] )
				node[0] += 1
		res = []
		for s in A:
			prefix = ''
			node = tree
			for c in s:
				if node[0] <= 1:
					res.append(prefix)
					break
				prefix += c
				node = node[1][c]
			else:
				res.append(s)
		return res

"""
input: ["zebra", "dog", "duck", "dot"]

Now we will build prefix tree and we will also store count of characters

                root
                /|
         (d, 3)/ |(z, 1)
              /  |
          Node1  Node2
           /|        \
     (o,2)/ |(u,1)    \(e,1)
         /  |          \
   Node1.1  Node1.2     Node2.1
      | \         \            \
(g,1) |  \ (t,1)   \(c,1)       \(b,1)
      |   \         \            \ 
    Leaf Leaf       Node1.2.1     Node2.1.1
    (dog)  (dot)        \                  \
                         \(k, 1)            \(r, 1)
                          \                  \   
                          Leaf               Node2.1.1.1
                          (duck)                       \
                                                        \(a,1)
                                                         \
                                                         Leaf
                                                         (zebra)

Now, for every leaf / word , we find the character nearest to the root with frequency as 1. 
The prefix that the path from root to this character corresponds to, is the representation of the word. 

"""