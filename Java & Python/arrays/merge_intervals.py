# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
    	if new_interval is None:
    		return None
    	new_start = new_interval.start
    	new_end = new_interval.end
    	start_interval, end_interval = -1, -1

    	for i in xrange(len(intervals)):
    		start = intervals[i].start    		
    		end = intervals[i].end

    		# fits inside existing intervals
    		if new_start >= start and new_start <= end:
    			start_interval = i
    		
    		if new_end >= start and new_end <= end:
    			end_interval = i

    	if start_interval == -1 and end_interval == -1:
    		start_interval = 0
    		for i in xrange(len(intervals)):
    			if new_start > intervals[i].end:
    				start_interval = i+1

			end_interval = len(intervals)-1
    		for i in xrange(len(intervals)-1, -1, -1):
    			if new_end < intervals[i].start:
    				end_interval = i-1
    		# merge
    		for i in xrange(start_interval, end_interval+1):
    			intervals.remove(start_interval)		# error right here
    		# insert new interval
    		intervals.insert(start_interval, new_interval)
    		return intervals

		if start_interval == -1:
			for i in xrange(len(intervals)-1, -1, -1):
				if new_start <= intervals[i].start:
					start_interval = i
		if end_interval == -1:
			for i in xrange(len(intervals)):
				if new_end >= intervals[i].end:
					end_interval = i

		new_start = min(intervals[start_interval].start, new_start)
		new_end = max(intervals[end_interval].end, new_end)

		intervals[start_interval].start = start
		intervals[start_interval].end = end

		# delete ones in between
		for i in xrange(start_interval+1, end_interval+1):
			intervals.remove(start_interval+1)

		# insert 
    	intervals.insert(start_interval, new_interval)
    	return intervals
"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
"""