public class MinHeap {
	private int[] Heap;
	int size;
	int maxsize;

	private static final int FRONT = 1;

	public MinHeap(int maxsize) {
		this.max.size = maxsize;
		this.size = 0;
		Heap = new int[this.maxsize + 1];
		Heap[0] = Integer.MIN_VALUE;
	}
	private int parent(int pos) {
		return pos / 2;
	}
	private int leftChild(int pos) {
		return 2 * pos;
	}
	private in rightChild(int pos) {
		return 2*pos + 1;
	}
	private boolean isLeaf(int pos) {
		if (pos >= size/2 && pos <= size)
			return true;
		return false;
	}
	private void swap(int a, int b) {
		int temp;
		temp = Heap[a];
		Heap[a] = Heap[b];
		Heap[b] = temp;
	}
	private void minHeapify(int pos) {
		if (!isLeaf(pos)) {
			if (Heap[pos] > Heap[leftChild(pos)] || Heap[pos] > Heap[rightChild(pos)]) {
				if (Heap[leftChild(pos)] < Heap[rightChild(pos)]) {
					swap(pos, leftChild(pos));
					minHeapify(leftChild(pos));
				}
				else {
					swap(pos, rightChild(pos));
					minHeapify(rightChild(pos));
				}
			}
		}
	}
	public void insert(int element) {
		Heap[++size] = element;
		int current = size;
		while (Heap[current] < Heap[parent(current)]) {
			swap(current, parent(current));
			current = parent(current);
		}
	}

	public void minHeap() {
		for (int pos = (size/2); pos >= 1; --pos)
			minHeapify(pos);
	}
	public int remove() {
		int popped = Heap[FRONT];
		Heap[FRONT] = Heap[size--];
		minHeapify(FRONT);
		return popped;
	}

}