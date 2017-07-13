#!/usr/bin/python2

# Quicksort: O(n log(n))
def quicksort(A):
	_quicksort(A, 0, len(A)-1)

def _quicksort(A, start, end):
	if start < end:
		split = partition(A, start, end)
		_quicksort(A, start, split-1)
		_quicksort(A, split+1, end)
def partition(A, start, end):
	pivot = A[end]
	left = start
	right = end
	while left < right:
		while A[left] < pivot:
			left += 1
		while A[right] > pivot:
			right -= 1
		A[left], A[right] = A[right], A[left]

		# if numbers are duplicates
		if A[left] == A[right]:
			left += 1
	return right

if __name__ == "__main__":
	array = [17, 9, 13, 8, 7, 7, -5, 6, 11, 3, 4, 1, 2]
	quicksort(array)
	print array