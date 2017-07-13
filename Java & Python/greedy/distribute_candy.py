# traverse forwards, check if [i] > [i-1]
# traverse backwards, check if [i] > [i+1], take max of candies[i] or [i+1]
class Solution:
	def candy(self, ratings):
		candies = [1] * len(ratings)

		for i in xrange(1, len(ratings)):
			if ratings[i] > ratings[i-1]:
				candies[i] = candies[i-1]+1
		for i in xrange(len(ratings)-2,-1,-1):
			if ratings[i] > ratings[i+1]:
				candies[i] = max(candies[i],candies[i+1]+1)
		return sum(candies)
"""
There are N children standing in a line. Each child is assigned a rating value.

 You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Sample Input :

Ratings : [1 2]
Sample Output :

3
The candidate with 1 rating gets 1 candy and candidate with rating cannot get 1 candy as 1 is its neighbor. So rating 2 candidate gets 2 candies. In total, 2+1 = 3 candies need to be given out.
"""
