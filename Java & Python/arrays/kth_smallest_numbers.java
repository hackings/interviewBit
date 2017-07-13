/** 
 * 17.14 - Smallest K
 * Design an algorithm to find the smallest K numbers in an array
 */
class PartitionResult {
	int leftSize, middleSize;
	public PartitionResult(int left, int middle) {
		this.leftSize = left;
		this.middleSize = middle;
	}
}
int[] smallestK(int[] array, int k) {
	if (k <= 0 || k > array.length)	
		throw new IllegalArgumentException();
	int threshold = rank(array,k-1);		// int[k]
	int[] smallest = new int[k];
	int count = 0;
	for (int a : array) {
		if (a < threshold) {
			smallest[count] = a;
			++count;
		}
	}
	while (count < k)
		smallest[count] = threshold; ++count;
	return smallest;
}
int rank(int[] array, int k) {
	if (k >= array.length)
		throw new IllegalArgumentException();
	return rank(array, k, 0, array.length-1);
}
int rank(int[] array, int k, int start, int end) {
	int pivot = array[randomIntInRange(start, end)];
	PartitionResult partition = partition(array, start, end, pivot);
	int leftSize = partition.leftSize;
	int middleSize = partition.middleSize;

	if (k < leftSize)
		return rank(array, k, start, start+leftSize-1);
	else if (k < leftSize + middleSize)
		return pivot;
	else
		return rank(array, k-leftSize-middleSize, start + leftSize + middleSize, end);
}

PartitionResult partition(int[] array, int start, int end, int pivot) {
	int left = start;
	int right = end;
	int middle = start;
	while (middle <= right) {
		if (array[middle] < pivot) {
			swap(array, middle, left);
			++middle; ++left;
		}
		else if (array[middle] > pivot) {
			swap(array, middle, right);
			--right;
		}
		else if (array[middle] == pivot)
			++middle;
	}
	return new Partition(left-start, right-left + 1);	// return size of left, middle
}

/* O(n) time

This is an optimization over method 1 if QuickSort is used as a sorting algorithm in first step. In QuickSort, we pick a pivot element, then move the pivot element to its correct position and partition the array around it. The idea is, not to do complete quicksort, but stop at the point where pivot itself is k’th smallest element. Also, not to recur for both left and right sides of pivot, but recur for one of them according to the position of pivot. The worst case time complexity of this method is O(n2), but it works in O(n) on average.
 */
