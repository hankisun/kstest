#include <stdio.h>

int Heap[10];
int len;

int compare(int a, int b) {
	if (a > b)
		return 1;
	else
		return 0;
}

void push(int n) {
	int cur, parent;

	Heap[len] = n;
	cur = len++;
	while ((parent = (cur + 1) / 2 - 1) >= 0) {
		if (compare(n, Heap[parent])) {
			Heap[cur] = Heap[parent];
			cur = parent;
		}
		else
			break;
	}
	Heap[cur] = n;
}

int pop() {
	int cur, left, right, child;
	int ret = Heap[0];
	int n;

	n = Heap[0] = Heap[--len];
	cur = 0;
	while ((left = cur * 2 + 1) < len) {
		if (left == len - 1)
			child = left;
		else {
			right = left + 1;
			if (compare(Heap[left], Heap[right]))
				child = left;
			else
				child = right;
		}
		if (compare(Heap[child], n)) {
			Heap[cur] = Heap[child];
			cur = child;
		}
		else
			break;
	}
	Heap[cur] = n;
	return ret;
}

void insertion(int arr[]) {
	int i, j;
	int n;
	for (i = 1; i < 10; i++) {
		n = arr[i];
		for (j = i - 1; j >= 0; j--) {
			if (compare(n, arr[j])) {
				arr[j + 1] = arr[j];
			}
			else
				break;
		}
		arr[j + 1] = n;
	}
}

int main() {
	int i;
	int arr[10] = { 6,4,2,1,3,5,9,8,7,10 };
	int arr2[10] = { 6,4,2,1,3,5,9,8,7,10 };

	for (i = 0; i < 10; i++) {
		push(arr[i]);
	}
	for (i = 0; i < 10; i++) {
		printf("%d ", pop());
	}
	printf("\n");

	insertion(arr2);
	for (i = 0; i < 10; i++)
		printf("%d ", arr2[i]);
	printf("\n");
}